"""Parse a pyi file using typed_ast."""

import dataclasses
import hashlib
import sys
import typing
from typing import Any, List, Optional, Tuple, Union

from pytype import utils
from pytype.ast import debug
from pytype.pyi import classdef
from pytype.pyi import conditions
from pytype.pyi import definitions
from pytype.pyi import evaluator
from pytype.pyi import function
from pytype.pyi import modules
from pytype.pyi import types
from pytype.pyi import visitor
from pytype.pytd import pep484
from pytype.pytd import pytd
from pytype.pytd import pytd_utils
from pytype.pytd import visitors
from pytype.pytd.codegen import decorate
from pytype.pytd.codegen import pytdgen
from typed_ast import ast3


_DEFAULT_PLATFORM = "linux"


# reexport as parser.ParseError
ParseError = types.ParseError


_TYPEVAR_IDS = ("TypeVar", "typing.TypeVar")
_PARAMSPEC_IDS = (
    "ParamSpec", "typing.ParamSpec", "typing_extensions.ParamSpec")
_TYPING_NAMEDTUPLE_IDS = ("NamedTuple", "typing.NamedTuple")
_COLL_NAMEDTUPLE_IDS = ("namedtuple", "collections.namedtuple")
_TYPEDDICT_IDS = (
    "TypedDict", "typing.TypedDict", "typing_extensions.TypedDict")
_NEWTYPE_IDS = ("NewType", "typing.NewType")
_ANNOTATED_IDS = (
    "Annotated", "typing.Annotated", "typing_extensions.Annotated")


#------------------------------------------------------
# imports


def _tuple_of_import(alias: ast3.AST) -> Tuple[str, str]:
  """Convert a typedast import into one that add_import expects."""
  if alias.asname is None:
    return alias.name
  return alias.name, alias.asname


def _import_from_module(module: Optional[str], level: int) -> str:
  """Convert a typedast import's 'from' into one that add_import expects."""
  if module is None:
    return {1: "__PACKAGE__", 2: "__PARENT__"}[level]
  prefix = "." * level
  return prefix + module


#------------------------------------------------------
# typevars


@dataclasses.dataclass
class _TypeVar:
  """Internal representation of typevars."""

  name: str
  bound: Optional[str]
  constraints: List[Any]

  @classmethod
  def from_call(cls, node: ast3.AST) -> "_TypeVar":
    """Construct a _TypeVar from an ast.Call node."""
    name, *constraints = node.args
    bound = None
    # 'bound' is the only keyword argument we currently use.
    # TODO(rechen): We should enforce the PEP 484 guideline that
    # len(constraints) != 1. However, this guideline is currently violated
    # in typeshed (see https://github.com/python/typeshed/pull/806).
    kws = {x.arg for x in node.keywords}
    extra = kws - {"bound", "covariant", "contravariant"}
    if extra:
      raise ParseError(f"Unrecognized keyword(s): {', '.join(extra)}")
    for kw in node.keywords:
      if kw.arg == "bound":
        bound = kw.value
    return cls(name, bound, constraints)


@dataclasses.dataclass
class _ParamSpec:
  """Internal representation of ParamSpecs."""

  name: str

  @classmethod
  def from_call(cls, node: ast3.AST) -> "_ParamSpec":
    name, = node.args
    return cls(name)


#------------------------------------------------------
# pytd utils

#------------------------------------------------------
# Main tree visitor and generator code


def _attribute_to_name(node: ast3.Attribute) -> ast3.Name:
  """Recursively convert Attributes to Names."""
  val = node.value
  if isinstance(val, ast3.Name):
    prefix = val.id
  elif isinstance(val, ast3.Attribute):
    prefix = _attribute_to_name(val).id
  elif isinstance(val, (pytd.NamedType, pytd.Module)):
    prefix = val.name
  else:
    msg = f"Unexpected attribute access on {val!r} [{type(val)}]"
    raise ParseError(msg)
  return ast3.Name(f"{prefix}.{node.attr}")


class AnnotationVisitor(visitor.BaseVisitor):
  """Converts typed_ast annotations to pytd."""

  def show(self, node):
    print(debug.dump(node, ast3, include_attributes=False))

  def convert_late_annotation(self, annotation):
    try:
      # Late annotations may need to be parsed into an AST first
      if annotation.isalpha():
        return self.defs.new_type(annotation)
      a = ast3.parse(annotation)
      # Unwrap the module the parser puts around the source string
      typ = a.body[0].value
      return self.visit(typ)
    except ParseError as e:
      # Clear out position information since it is relative to the typecomment
      e.clear_position()
      raise e

  def convert_metadata(self, node):
    ret = MetadataVisitor().visit(node)
    return ret if ret is not None else node

  def visit_Constant(self, node):
    # Handle a types.Constant node (converted from a literal constant).
    # We do not handle the mixed case
    #   x: List['int']
    # since we need to not convert subscripts for typing.Literal, i.e.
    #   x: Literal['int']
    # pyi files do not require quoting forward references anyway, so we keep the
    # code simple here and just handle the basic case of a fully quoted type.
    if node.type == "str" and not self.subscripted:
      return self.convert_late_annotation(node.value)

  def visit_Tuple(self, node):
    return tuple(node.elts)

  def visit_List(self, node):
    return list(node.elts)

  def visit_Name(self, node):
    if self.subscripted and (node is self.subscripted[-1]):
      # This is needed because
      #   Foo[X]
      # parses to
      #   Subscript(Name(id = Foo), Name(id = X))
      # so we see visit_Name(Foo) before visit_Subscript(Foo[X]).
      # If Foo resolves to a generic type we want to know if it is being passed
      # params in this context (in which case we simply resolve the type here,
      # and create a new type when we get the param list in visit_Subscript) or
      # if it is just being used as a bare Foo, in which case we need to create
      # the new type Foo[Any] below.
      return self.defs.resolve_type(node.id)
    else:
      return self.defs.new_type(node.id)

  def _convert_typing_annotated(self, node):
    typ, *args = node.slice.value.elts
    typ = self.visit(typ)
    params = (self.convert_metadata(x) for x in args)
    node.slice.value = (typ,) + tuple(params)

  def enter_Subscript(self, node):
    if isinstance(node.value, ast3.Attribute):
      node.value = _attribute_to_name(node.value).id
    if getattr(node.value, "id", None) in _ANNOTATED_IDS:
      self._convert_typing_annotated(node)
    self.subscripted.append(node.value)

  def visit_Subscript(self, node):
    params = node.slice.value
    if type(params) is not tuple:  # pylint: disable=unidiomatic-typecheck
      params = (params,)
    return self.defs.new_type(node.value, params)

  def leave_Subscript(self, node):
    self.subscripted.pop()

  def visit_Attribute(self, node):
    annotation = _attribute_to_name(node).id
    return self.defs.new_type(annotation)

  def visit_BinOp(self, node):
    if isinstance(node.op, ast3.BitOr):
      return self.defs.new_type("typing.Union", [node.left, node.right])
    else:
      raise ParseError(f"Unexpected operator {node.op}")

  def visit_BoolOp(self, node):
    if isinstance(node.op, ast3.Or):
      raise ParseError("Deprecated syntax `x or y`; use `Union[x, y]` instead")
    else:
      raise ParseError(f"Unexpected operator {node.op}")


class MetadataVisitor(visitor.BaseVisitor):
  """Converts typing.Annotated metadata."""

  def visit_Call(self, node):
    posargs = tuple(evaluator.literal_eval(x) for x in node.args)
    kwargs = {x.arg: evaluator.literal_eval(x.value) for x in node.keywords}
    return (node.func.id, posargs, kwargs)

  def visit_Dict(self, node):
    return evaluator.literal_eval(node)


def _flatten_splices(body: List[Any]) -> List[Any]:
  """Flatten a list with nested Splices."""
  if not any(isinstance(x, Splice) for x in body):
    return body
  out = []
  for x in body:
    if isinstance(x, Splice):
      # This technically needn't be recursive because of how we build Splices
      # but better not to have the class assume that.
      out.extend(_flatten_splices(x.body))
    else:
      out.append(x)
  return out


class Splice:
  """Splice a list into a node body."""

  def __init__(self, body):
    self.body = _flatten_splices(body)

  def __str__(self):
    return "Splice(\n" + ",\n  ".join([str(x) for x in self.body]) + "\n)"

  def __repr__(self):
    return str(self)


class GeneratePytdVisitor(visitor.BaseVisitor):
  """Converts a typed_ast tree to a pytd tree."""

  def __init__(self, src, filename, module_name, version, platform):
    defs = definitions.Definitions(modules.Module(filename, module_name))
    super().__init__(defs=defs, filename=filename)
    self.src_code = src
    self.module_name = module_name
    self.version = version
    self.platform = platform or _DEFAULT_PLATFORM
    self.level = 0
    self.in_function = False  # pyi will not have nested defs
    self.annotation_visitor = AnnotationVisitor(defs=defs, filename=filename)
    self.class_stack = []

  def show(self, node):
    print(debug.dump(node, ast3, include_attributes=False))

  def convert_node(self, node):
    # Converting a node via a visitor will convert the subnodes, but if the
    # argument node itself needs conversion, we need to use the pattern
    #   node = annotation_visitor.visit(node)
    # However, the AnnotationVisitor returns None if it does not trigger on the
    # root node it is passed, so call it via this method instead.
    ret = self.annotation_visitor.visit(node)
    return ret if ret is not None else node

  def convert_node_annotations(self, node):
    """Transform type annotations to pytd."""
    if getattr(node, "annotation", None):
      node.annotation = self.convert_node(node.annotation)
    elif getattr(node, "type_comment", None):
      node.type_comment = self.annotation_visitor.convert_late_annotation(
          node.type_comment)

  def resolve_name(self, name):
    """Resolve an alias or create a NamedType."""
    return self.defs.type_map.get(name) or pytd.NamedType(name)

  def visit_Module(self, node):
    node.body = _flatten_splices(node.body)
    return self.defs.build_type_decl_unit(node.body)

  def visit_Pass(self, node):
    return self.defs.ELLIPSIS

  def visit_Expr(self, node):
    # Handle some special cases of expressions that can occur in class and
    # module bodies.
    if node.value == self.defs.ELLIPSIS:
      # class x: ...
      return node.value
    elif types.Constant.is_str(node.value):
      # docstrings
      return Splice([])

  def visit_arg(self, node):
    self.convert_node_annotations(node)

  def _get_name(self, node):
    if isinstance(node, ast3.Name):
      return node.id
    elif isinstance(node, ast3.Attribute):
      return f"{node.value.id}.{node.attr}"
    else:
      raise ParseError(f"Unexpected node type in get_name: {node}")

  def _preprocess_decorator_list(self, node):
    decorators = []
    for d in node.decorator_list:
      if isinstance(d, (ast3.Name, ast3.Attribute)):
        decorators.append(self._get_name(d))
      elif isinstance(d, ast3.Call):
        decorators.append(self._get_name(d.func))
      else:
        raise ParseError(f"Unexpected decorator: {d}")
    node.decorator_list = decorators

  def _preprocess_function(self, node):
    node.args = self.convert_node(node.args)
    node.returns = self.convert_node(node.returns)
    self._preprocess_decorator_list(node)
    node.body = _flatten_splices(node.body)

  def visit_FunctionDef(self, node):
    self._preprocess_function(node)
    return function.NameAndSig.from_function(node, False)

  def visit_AsyncFunctionDef(self, node):
    self._preprocess_function(node)
    return function.NameAndSig.from_function(node, True)

  def new_alias_or_constant(self, name, value):
    """Build an alias or constant."""
    # This is here rather than in _Definitions because we need to build a
    # constant or alias from a partially converted typed_ast subtree.
    if name == "__slots__":
      if not (isinstance(value, ast3.List) and
              all(types.Constant.is_str(x) for x in value.elts)):
        raise ParseError("__slots__ must be a list of strings")
      return types.SlotDecl(tuple(x.value for x in value.elts))
    elif isinstance(value, types.Constant):
      return pytd.Constant(name, value.to_pytd())
    elif isinstance(value, types.Ellipsis):
      return pytd.Constant(name, pytd.AnythingType())
    elif isinstance(value, pytd.NamedType):
      res = self.defs.resolve_type(value.name)
      return pytd.Alias(name, res)
    elif isinstance(value, ast3.List):
      if name != "__all__":
        raise ParseError("Only __slots__ and __all__ can be literal lists")
      return pytd.Constant(name, pytdgen.pytd_list("str"))
    elif isinstance(value, ast3.Tuple):
      # TODO(mdemello): Consistent with the current parser, but should it
      # properly be Tuple[Type]?
      return pytd.Constant(name, pytd.NamedType("tuple"))
    elif isinstance(value, ast3.Name):
      value = self.defs.resolve_type(value.id)
      return pytd.Alias(name, value)
    else:
      # TODO(mdemello): add a case for TypeVar()
      # Convert any complex type aliases
      value = self.convert_node(value)
      return pytd.Alias(name, value)

  def enter_AnnAssign(self, node):
    self.convert_node_annotations(node)

  def visit_AnnAssign(self, node):
    self.convert_node_annotations(node)
    name = node.target.id
    typ = node.annotation
    val = self.convert_node(node.value)
    if val and not types.is_any(val):
      msg = f"Default value for {name}: {typ.name} can only be '...', got {val}"
      raise ParseError(msg)
    return pytd.Constant(name, typ, val)

  def _assign(self, node, target, value):
    name = target.id

    # Record and erase TypeVar and ParamSpec definitions.
    if isinstance(value, _TypeVar):
      self.defs.add_type_var(name, value)
      return Splice([])
    elif isinstance(value, _ParamSpec):
      self.defs.add_param_spec(name, value)
      return Splice([])

    if node.type_comment:
      # TODO(mdemello): can pyi files have aliases with typecomments?
      ret = pytd.Constant(name, node.type_comment)
    else:
      ret = self.new_alias_or_constant(name, value)

    if self.in_function:
      # Should never happen, but this keeps pytype happy.
      if isinstance(ret, types.SlotDecl):
        raise ParseError("Cannot change the type of __slots__")
      return function.Mutator(name, ret.type)

    if self.level == 0:
      self.defs.add_alias_or_constant(ret)
    return ret

  def visit_Assign(self, node):
    self.convert_node_annotations(node)
    out = []
    value = node.value
    for target in node.targets:
      if isinstance(target, ast3.Tuple):
        count = len(target.elts)
        if not (isinstance(value, ast3.Tuple) and count == len(value.elts)):
          msg = f"Cannot unpack {count} values for multiple assignment"
          raise ParseError(msg)
        for k, v in zip(target.elts, value.elts):
          out.append(self._assign(node, k, v))
      else:
        out.append(self._assign(node, target, value))
    return Splice(out)

  def visit_ClassDef(self, node):
    full_class_name = ".".join(self.class_stack)
    self.defs.type_map[full_class_name] = pytd.NamedType(full_class_name)

    # Convert decorators to named types
    self._preprocess_decorator_list(node)
    decorators = classdef.get_decorators(
        node.decorator_list, self.defs.type_map)

    self.annotation_visitor.visit(node.bases)
    self.annotation_visitor.visit(node.keywords)
    defs = _flatten_splices(node.body)
    return self.defs.build_class(
        node.name, node.bases, node.keywords, decorators, defs)

  def enter_If(self, node):
    # Evaluate the test and preemptively remove the invalid branch so we don't
    # waste time traversing it.
    node.test = conditions.evaluate(node.test, self.version, self.platform)
    if not isinstance(node.test, bool):
      raise ParseError("Unexpected if statement" + debug.dump(node, ast3))

    if node.test:
      node.orelse = []
    else:
      node.body = []

  def visit_If(self, node):
    if not isinstance(node.test, bool):
      raise ParseError("Unexpected if statement" + debug.dump(node, ast3))

    if node.test:
      return Splice(node.body)
    else:
      return Splice(node.orelse)

  def visit_Import(self, node):
    if self.level > 0:
      raise ParseError("Import statements need to be at module level")
    imports = [_tuple_of_import(x) for x in node.names]
    self.defs.add_import(None, imports)
    return Splice([])

  def visit_ImportFrom(self, node):
    if self.level > 0:
      raise ParseError("Import statements need to be at module level")
    imports = [_tuple_of_import(x) for x in node.names]
    module = _import_from_module(node.module, node.level)
    self.defs.add_import(module, imports)
    return Splice([])

  def _convert_newtype_args(self, node: ast3.AST):
    if len(node.args) != 2:
      msg = "Wrong args: expected NewType(name, [(field, type), ...])"
      raise ParseError(msg)
    name, typ = node.args
    typ = self.convert_node(typ)
    node.args = [name.s, typ]

  def _convert_typing_namedtuple_args(self, node: ast3.AST):
    # TODO(mdemello): handle NamedTuple("X", a=int, b=str, ...)
    if len(node.args) != 2:
      msg = "Wrong args: expected NamedTuple(name, [(field, type), ...])"
      raise ParseError(msg)
    name, fields = node.args
    fields = self.convert_node(fields)
    fields = [(types.string_value(n), t) for (n, t) in fields]
    node.args = [name.s, fields]

  def _convert_collections_namedtuple_args(self, node: ast3.AST):
    if len(node.args) != 2:
      msg = "Wrong args: expected namedtuple(name, [field, ...])"
      raise ParseError(msg)
    name, fields = node.args
    fields = self.convert_node(fields)
    fields = [(types.string_value(n), pytd.AnythingType()) for n in fields]
    node.args = [name.s, fields]

  def _convert_typevar_args(self, node):
    self.annotation_visitor.visit(node.keywords)
    if not node.args:
      raise ParseError("Missing arguments to TypeVar")
    name, *rest = node.args
    if not isinstance(name, ast3.Str):
      raise ParseError("Bad arguments to TypeVar")
    node.args = [name.s] + [self.convert_node(x) for x in rest]
    # Special-case late types in bound since typeshed uses it.
    for kw in node.keywords:
      if kw.arg == "bound":
        if isinstance(kw.value, types.Constant):
          val = types.string_value(kw.value, context="TypeVar bound")
          kw.value = self.annotation_visitor.convert_late_annotation(val)

  def _convert_paramspec_args(self, node):
    name, = node.args
    node.args = [name.s]

  def _convert_typed_dict_args(self, node: ast3.AST):
    # TODO(b/157603915): new_typed_dict currently doesn't do anything with the
    # args, so we don't bother converting them fully.
    msg = "Wrong args: expected TypedDict(name, {field: type, ...})"
    if len(node.args) != 2:
      raise ParseError(msg)
    name, fields = node.args
    if not (isinstance(name, ast3.Str) and isinstance(fields, ast3.Dict)):
      raise ParseError(msg)

  def enter_Call(self, node):
    # Some function arguments need to be converted from strings to types when
    # entering the node, rather than bottom-up when they would already have been
    # converted to types.Constant.
    # We also convert some literal string nodes that are not meant to be types
    # (e.g. the first arg to TypeVar()) to their bare values since we are
    # passing them to internal functions directly in visit_Call.
    if isinstance(node.func, ast3.Attribute):
      node.func = _attribute_to_name(node.func)
    if node.func.id in _TYPEVAR_IDS:
      self._convert_typevar_args(node)
    elif node.func.id in _PARAMSPEC_IDS:
      self._convert_paramspec_args(node)
    elif node.func.id in _TYPING_NAMEDTUPLE_IDS:
      self._convert_typing_namedtuple_args(node)
    elif node.func.id in _COLL_NAMEDTUPLE_IDS:
      self._convert_collections_namedtuple_args(node)
    elif node.func.id in _TYPEDDICT_IDS:
      self._convert_typed_dict_args(node)
    elif node.func.id in _NEWTYPE_IDS:
      return self._convert_newtype_args(node)

  def visit_Call(self, node):
    if node.func.id in _TYPEVAR_IDS:
      if self.level > 0:
        raise ParseError("TypeVars need to be defined at module level")
      return _TypeVar.from_call(node)
    elif node.func.id in _PARAMSPEC_IDS:
      return _ParamSpec.from_call(node)
    elif node.func.id in _TYPING_NAMEDTUPLE_IDS + _COLL_NAMEDTUPLE_IDS:
      return self.defs.new_named_tuple(*node.args)
    elif node.func.id in _TYPEDDICT_IDS:
      return self.defs.new_typed_dict(*node.args, total=False)
    elif node.func.id in _NEWTYPE_IDS:
      return self.defs.new_new_type(*node.args)
    # Convert all other calls to NamedTypes; for example:
    # * typing.pyi uses things like
    #     List = _Alias()
    # * pytd extensions allow both
    #     raise Exception
    #   and
    #     raise Exception()
    return pytd.NamedType(node.func.id)

  def visit_Raise(self, node):
    ret = self.convert_node(node.exc)
    return types.Raise(ret)

  # Track nesting level

  def enter_FunctionDef(self, node):
    self.level += 1
    self.in_function = True

  def leave_FunctionDef(self, node):
    self.level -= 1
    self.in_function = False

  def enter_AsyncFunctionDef(self, node):
    self.enter_FunctionDef(node)

  def leave_AsyncFunctionDef(self, node):
    self.leave_FunctionDef(node)

  def enter_ClassDef(self, node):
    self.level += 1
    self.class_stack.append(node.name)

  def leave_ClassDef(self, node):
    self.level -= 1
    self.class_stack.pop()


def post_process_ast(ast, src, name=None):
  """Post-process the parsed AST."""
  ast = definitions.finalize_ast(ast)
  ast = ast.Visit(pep484.ConvertTypingToNative(name))

  if name:
    ast = ast.Replace(name=name)
    ast = ast.Visit(visitors.AddNamePrefix())
  else:
    # If there's no unique name, hash the sourcecode.
    ast = ast.Replace(name=hashlib.md5(src.encode("utf-8")).hexdigest())
  ast = ast.Visit(visitors.StripExternalNamePrefix())

  # Now that we have resolved external names, validate any class decorators that
  # do code generation. (We will generate the class lazily, but we should check
  # for errors at parse time so they can be reported early.)
  try:
    ast = ast.Visit(decorate.ValidateDecoratedClassVisitor())
  except TypeError as e:
    # Convert errors into ParseError. Unfortunately we no longer have location
    # information if an error is raised during transformation of a class node.
    raise ParseError.from_exc(e)

  # Typeshed files that explicitly import and refer to "__builtin__" need to
  # have that rewritten to builtins
  ast = ast.Visit(visitors.RenameBuiltinsPrefix())

  return ast


def _parse(src: str, feature_version: int, filename: str = ""):
  """Call the typed_ast parser with the appropriate feature version."""
  try:
    ast_root_node = ast3.parse(src, filename, feature_version=feature_version)
  except SyntaxError as e:
    raise ParseError(e.msg, line=e.lineno, filename=filename) from e
  return ast_root_node


# Python version input type.
VersionType = Union[int, Tuple[int, ...]]


def _feature_version(python_version: VersionType) -> int:
  """Get the python feature version for the parser."""
  if isinstance(python_version, int):
    return sys.version_info.minor
  else:
    python_version = typing.cast(Tuple[int, ...], python_version)
    if len(python_version) == 1:
      return sys.version_info.minor
    else:
      return python_version[1]


def parse_string(
    src: str,
    python_version: VersionType = 3,
    name: Optional[str] = None,
    filename: Optional[str] = None,
    platform: Optional[str] = None
):
  return parse_pyi(src, filename=filename, module_name=name,
                   platform=platform, python_version=python_version)


def parse_pyi(
    src: str,
    filename: Optional[str],
    module_name: str,
    python_version: VersionType = 3,
    platform: Optional[str] = None
) -> pytd.TypeDeclUnit:
  """Parse a pyi string."""
  filename = filename or ""
  feature_version = _feature_version(python_version)
  python_version = utils.normalize_version(python_version)
  root = _parse(src, feature_version, filename)
  gen_pytd = GeneratePytdVisitor(
      src, filename, module_name, python_version, platform)
  root = gen_pytd.visit(root)
  root = post_process_ast(root, src, module_name)
  return root


def parse_pyi_debug(
    src: str,
    filename: str,
    module_name: str,
    python_version: VersionType = 3,
    platform: Optional[str] = None
) -> Tuple[pytd.TypeDeclUnit, GeneratePytdVisitor]:
  """Debug version of parse_pyi."""
  feature_version = _feature_version(python_version)
  python_version = utils.normalize_version(python_version)
  root = _parse(src, feature_version, filename)
  print(debug.dump(root, ast3, include_attributes=False))
  gen_pytd = GeneratePytdVisitor(
      src, filename, module_name, python_version, platform)
  root = gen_pytd.visit(root)
  print("---transformed parse tree--------------------")
  print(root)
  root = post_process_ast(root, src, module_name)
  print("---post-processed---------------------")
  print(root)
  print("------------------------")
  print(gen_pytd.defs.type_map)
  print(gen_pytd.defs.module_path_map)
  return root, gen_pytd


def canonical_pyi(pyi, python_version=3, multiline_args=False):
  """Rewrite a pyi in canonical form."""
  ast = parse_string(pyi, python_version=python_version)
  ast = ast.Visit(visitors.ClassTypeToNamedType())
  ast = ast.Visit(visitors.CanonicalOrderingVisitor(sort_signatures=True))
  ast.Visit(visitors.VerifyVisitor())
  return pytd_utils.Print(ast, multiline_args)
