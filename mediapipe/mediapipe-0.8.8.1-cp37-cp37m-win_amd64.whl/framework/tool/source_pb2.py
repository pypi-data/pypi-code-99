# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/tool/source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/tool/source.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n%mediapipe/framework/tool/source.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xfa\x02\n%SidePacketsToStreamsCalculatorOptions\x12\x15\n\nnum_inputs\x18\x01 \x01(\x05:\x01\x31\x12\x66\n\rset_timestamp\x18\x02 \x01(\x0e\x32\x41.mediapipe.SidePacketsToStreamsCalculatorOptions.SetTimestampMode:\x0cVECTOR_INDEX\x12 \n\x12vectors_of_packets\x18\x03 \x01(\x08:\x04true\"P\n\x10SetTimestampMode\x12\x10\n\x0cVECTOR_INDEX\x10\x00\x12\x0e\n\nPRE_STREAM\x10\x01\x12\x10\n\x0cWHOLE_STREAM\x10\x02\x12\x08\n\x04NONE\x10\x03\x32^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb7\x8c\x8a\x1d \x01(\x0b\x32\x30.mediapipe.SidePacketsToStreamsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS_SETTIMESTAMPMODE = _descriptor.EnumDescriptor(
  name='SetTimestampMode',
  full_name='mediapipe.SidePacketsToStreamsCalculatorOptions.SetTimestampMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VECTOR_INDEX', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_STREAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHOLE_STREAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=293,
  serialized_end=373,
)
_sym_db.RegisterEnumDescriptor(_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS_SETTIMESTAMPMODE)


_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='SidePacketsToStreamsCalculatorOptions',
  full_name='mediapipe.SidePacketsToStreamsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_inputs', full_name='mediapipe.SidePacketsToStreamsCalculatorOptions.num_inputs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_timestamp', full_name='mediapipe.SidePacketsToStreamsCalculatorOptions.set_timestamp', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vectors_of_packets', full_name='mediapipe.SidePacketsToStreamsCalculatorOptions.vectors_of_packets', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.SidePacketsToStreamsCalculatorOptions.ext', index=0,
      number=60982839, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS_SETTIMESTAMPMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=469,
)

_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS.fields_by_name['set_timestamp'].enum_type = _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS_SETTIMESTAMPMODE
_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS_SETTIMESTAMPMODE.containing_type = _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['SidePacketsToStreamsCalculatorOptions'] = _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS

SidePacketsToStreamsCalculatorOptions = _reflection.GeneratedProtocolMessageType('SidePacketsToStreamsCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS,
  __module__ = 'mediapipe.framework.tool.source_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SidePacketsToStreamsCalculatorOptions)
  ))
_sym_db.RegisterMessage(SidePacketsToStreamsCalculatorOptions)

_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SIDEPACKETSTOSTREAMSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SIDEPACKETSTOSTREAMSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
