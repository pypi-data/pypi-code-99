from shlex import split as strSplit

from . utils import chkSeqOfLen, isNum
from . import bar
from . sets import ColorSetEntry, FormatSetEntry, CharSetEntry, FormatSet

_OP_EQU = "=="
_OP_NEQ = "!="
_OP_GTR = ">"
_OP_LSS = "<"
_OP_GEQ = ">="
_OP_LEQ = "<="
_OP_IN = "<-"


class Cond:
	"""Condition manager used by a PBar object."""
	def __init__(self, condition: str, charset: CharSetEntry = None,
				 colorset: ColorSetEntry = None, formatset: FormatSetEntry = None) -> None:
		"""
		Apply different customization sets to a bar if the condition supplied succeeds.
		Text comparisons are case insensitive.

		The condition string must be composed of three values separated by spaces:

		1. Attribute key (Formatting keys for `pbar.FormatSet`)
		2. Comparison operator (`==`, `!=`, `>`, `<`, `>=`, `<=`, `<-`)
		3. Value

		- Note: The "custom" operator `<-` stands for the attribute key containing the value.

		---

		### Examples:

		>>> Cond("percentage >= 50", colorset=ColorSet.DARVIL)

		>>> Cond("text <- 'error'", colorset=ColorSet.ERROR, formatset=FormatSet.TITLE_SUBTITLE)
		"""
		vs = strSplit(condition)
		chkSeqOfLen(vs, 3, "condition")
		self.attribute, self.operator = vs[0:2]
		self.value = float(vs[2]) if isNum(vs[2]) else vs[2].lower()
		self.newSets = (charset, colorset, formatset)


	def __repr__(self) -> str:
		"""Returns `Cond('attrib operator value', *newSets)`"""
		return (f"{self.__class__.__name__}('{self.attribute} {self.operator} {self.value}', {self.newSets})")


	def test(self, cls: "bar.PBar") -> bool:
		"""Check if the condition succeededs with the values of the PBar object"""
		op = self.operator
		val = FormatSet._getBarAttrs(cls, self.attribute)
		val = val.lower() if isinstance(val, str) else val

		if op == _OP_EQU:
			return val == self.value
		elif op == _OP_NEQ:
			return val != self.value
		elif op == _OP_GTR:
			return val > self.value
		elif op == _OP_LSS:
			return val < self.value
		elif op == _OP_GEQ:
			return val >= self.value
		elif op == _OP_LEQ:
			return val <= self.value
		elif op == _OP_IN:
			return self.value in val
		else:
			raise RuntimeError(f"Invalid operator {op!r}")