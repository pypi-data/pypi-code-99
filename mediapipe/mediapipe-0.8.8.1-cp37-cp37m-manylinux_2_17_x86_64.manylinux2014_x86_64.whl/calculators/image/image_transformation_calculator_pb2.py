# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/image_transformation_calculator.proto

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
from mediapipe.gpu import scale_mode_pb2 as mediapipe_dot_gpu_dot_scale__mode__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/image/image_transformation_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nAmediapipe/calculators/image/image_transformation_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/scale_mode.proto\"h\n\x0cRotationMode\"X\n\x04Mode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nROTATION_0\x10\x01\x12\x0f\n\x0bROTATION_90\x10\x02\x12\x10\n\x0cROTATION_180\x10\x03\x12\x10\n\x0cROTATION_270\x10\x04\"\xfe\x02\n$ImageTransformationCalculatorOptions\x12\x17\n\x0coutput_width\x18\x01 \x01(\x05:\x01\x30\x12\x18\n\routput_height\x18\x02 \x01(\x05:\x01\x30\x12\x33\n\rrotation_mode\x18\x03 \x01(\x0e\x32\x1c.mediapipe.RotationMode.Mode\x12\x1e\n\x0f\x66lip_vertically\x18\x04 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x66lip_horizontally\x18\x05 \x01(\x08:\x05\x66\x61lse\x12-\n\nscale_mode\x18\x06 \x01(\x0e\x32\x19.mediapipe.ScaleMode.Mode\x12\x1e\n\x10\x63onstant_padding\x18\x07 \x01(\x08:\x04true2]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbe\xfd\x91x \x01(\x0b\x32/.mediapipe.ImageTransformationCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_scale__mode__pb2.DESCRIPTOR,])



_ROTATIONMODE_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='mediapipe.RotationMode.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATION_0', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATION_90', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATION_180', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROTATION_270', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=166,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_ROTATIONMODE_MODE)


_ROTATIONMODE = _descriptor.Descriptor(
  name='RotationMode',
  full_name='mediapipe.RotationMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROTATIONMODE_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=254,
)


_IMAGETRANSFORMATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ImageTransformationCalculatorOptions',
  full_name='mediapipe.ImageTransformationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_width', full_name='mediapipe.ImageTransformationCalculatorOptions.output_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_height', full_name='mediapipe.ImageTransformationCalculatorOptions.output_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_mode', full_name='mediapipe.ImageTransformationCalculatorOptions.rotation_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flip_vertically', full_name='mediapipe.ImageTransformationCalculatorOptions.flip_vertically', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flip_horizontally', full_name='mediapipe.ImageTransformationCalculatorOptions.flip_horizontally', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale_mode', full_name='mediapipe.ImageTransformationCalculatorOptions.scale_mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constant_padding', full_name='mediapipe.ImageTransformationCalculatorOptions.constant_padding', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ImageTransformationCalculatorOptions.ext', index=0,
      number=251952830, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=257,
  serialized_end=639,
)

_ROTATIONMODE_MODE.containing_type = _ROTATIONMODE
_IMAGETRANSFORMATIONCALCULATOROPTIONS.fields_by_name['rotation_mode'].enum_type = _ROTATIONMODE_MODE
_IMAGETRANSFORMATIONCALCULATOROPTIONS.fields_by_name['scale_mode'].enum_type = mediapipe_dot_gpu_dot_scale__mode__pb2._SCALEMODE_MODE
DESCRIPTOR.message_types_by_name['RotationMode'] = _ROTATIONMODE
DESCRIPTOR.message_types_by_name['ImageTransformationCalculatorOptions'] = _IMAGETRANSFORMATIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RotationMode = _reflection.GeneratedProtocolMessageType('RotationMode', (_message.Message,), dict(
  DESCRIPTOR = _ROTATIONMODE,
  __module__ = 'mediapipe.calculators.image.image_transformation_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RotationMode)
  ))
_sym_db.RegisterMessage(RotationMode)

ImageTransformationCalculatorOptions = _reflection.GeneratedProtocolMessageType('ImageTransformationCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _IMAGETRANSFORMATIONCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.image.image_transformation_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ImageTransformationCalculatorOptions)
  ))
_sym_db.RegisterMessage(ImageTransformationCalculatorOptions)

_IMAGETRANSFORMATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _IMAGETRANSFORMATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGETRANSFORMATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
