# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/image_to_tensor_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/tensor/image_to_tensor_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n=mediapipe/calculators/tensor/image_to_tensor_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xa3\x04\n\x1eImageToTensorCalculatorOptions\x12\x1b\n\x13output_tensor_width\x18\x01 \x01(\x05\x12\x1c\n\x14output_tensor_height\x18\x02 \x01(\x05\x12\x19\n\x11keep_aspect_ratio\x18\x03 \x01(\x08\x12Y\n\x19output_tensor_float_range\x18\x04 \x01(\x0b\x32\x34.mediapipe.ImageToTensorCalculatorOptions.FloatRangeH\x00\x12-\n\ngpu_origin\x18\x05 \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12I\n\x0b\x62order_mode\x18\x06 \x01(\x0e\x32\x34.mediapipe.ImageToTensorCalculatorOptions.BorderMode\x1a&\n\nFloatRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"K\n\nBorderMode\x12\x16\n\x12\x42ORDER_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42ORDER_ZERO\x10\x01\x12\x14\n\x10\x42ORDER_REPLICATE\x10\x02\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd3\xea\xb7\x9f\x01 \x01(\x0b\x32).mediapipe.ImageToTensorCalculatorOptionsB\x07\n\x05range')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_gpu__origin__pb2.DESCRIPTOR,])



_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE = _descriptor.EnumDescriptor(
  name='BorderMode',
  full_name='mediapipe.ImageToTensorCalculatorOptions.BorderMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BORDER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BORDER_ZERO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BORDER_REPLICATE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=520,
  serialized_end=595,
)
_sym_db.RegisterEnumDescriptor(_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE)


_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE = _descriptor.Descriptor(
  name='FloatRange',
  full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange.min', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange.max', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=518,
)

_IMAGETOTENSORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ImageToTensorCalculatorOptions',
  full_name='mediapipe.ImageToTensorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_tensor_width', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_tensor_height', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_aspect_ratio', full_name='mediapipe.ImageToTensorCalculatorOptions.keep_aspect_ratio', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_tensor_float_range', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_float_range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_origin', full_name='mediapipe.ImageToTensorCalculatorOptions.gpu_origin', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border_mode', full_name='mediapipe.ImageToTensorCalculatorOptions.border_mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ImageToTensorCalculatorOptions.ext', index=0,
      number=334361939, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE, ],
  enum_types=[
    _IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='range', full_name='mediapipe.ImageToTensorCalculatorOptions.range',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=147,
  serialized_end=694,
)

_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'].message_type = _IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['gpu_origin'].enum_type = mediapipe_dot_gpu_dot_gpu__origin__pb2._GPUORIGIN_MODE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['border_mode'].enum_type = _IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE
_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range'].fields.append(
  _IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'])
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'].containing_oneof = _IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range']
DESCRIPTOR.message_types_by_name['ImageToTensorCalculatorOptions'] = _IMAGETOTENSORCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageToTensorCalculatorOptions = _reflection.GeneratedProtocolMessageType('ImageToTensorCalculatorOptions', (_message.Message,), dict(

  FloatRange = _reflection.GeneratedProtocolMessageType('FloatRange', (_message.Message,), dict(
    DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE,
    __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions.FloatRange)
    ))
  ,
  DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions)
  ))
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions)
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions.FloatRange)

_IMAGETOTENSORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _IMAGETOTENSORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGETOTENSORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
