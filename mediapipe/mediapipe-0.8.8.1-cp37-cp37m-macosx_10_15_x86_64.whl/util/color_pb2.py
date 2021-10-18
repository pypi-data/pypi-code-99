# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/color.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/color.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1amediapipe/util/color.proto\x12\tmediapipe\"(\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\x05\x12\t\n\x01g\x18\x02 \x01(\x05\x12\t\n\x01\x62\x18\x03 \x01(\x05\"\x90\x01\n\x08\x43olorMap\x12=\n\x0elabel_to_color\x18\x01 \x03(\x0b\x32%.mediapipe.ColorMap.LabelToColorEntry\x1a\x45\n\x11LabelToColorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.mediapipe.Color:\x02\x38\x01'
)




_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='mediapipe.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='mediapipe.Color.r', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g', full_name='mediapipe.Color.g', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='mediapipe.Color.b', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=41,
  serialized_end=81,
)


_COLORMAP_LABELTOCOLORENTRY = _descriptor.Descriptor(
  name='LabelToColorEntry',
  full_name='mediapipe.ColorMap.LabelToColorEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mediapipe.ColorMap.LabelToColorEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mediapipe.ColorMap.LabelToColorEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=228,
)

_COLORMAP = _descriptor.Descriptor(
  name='ColorMap',
  full_name='mediapipe.ColorMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_to_color', full_name='mediapipe.ColorMap.label_to_color', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COLORMAP_LABELTOCOLORENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=228,
)

_COLORMAP_LABELTOCOLORENTRY.fields_by_name['value'].message_type = _COLOR
_COLORMAP_LABELTOCOLORENTRY.containing_type = _COLORMAP
_COLORMAP.fields_by_name['label_to_color'].message_type = _COLORMAP_LABELTOCOLORENTRY
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.message_types_by_name['ColorMap'] = _COLORMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), {
  'DESCRIPTOR' : _COLOR,
  '__module__' : 'mediapipe.util.color_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Color)
  })
_sym_db.RegisterMessage(Color)

ColorMap = _reflection.GeneratedProtocolMessageType('ColorMap', (_message.Message,), {

  'LabelToColorEntry' : _reflection.GeneratedProtocolMessageType('LabelToColorEntry', (_message.Message,), {
    'DESCRIPTOR' : _COLORMAP_LABELTOCOLORENTRY,
    '__module__' : 'mediapipe.util.color_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ColorMap.LabelToColorEntry)
    })
  ,
  'DESCRIPTOR' : _COLORMAP,
  '__module__' : 'mediapipe.util.color_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ColorMap)
  })
_sym_db.RegisterMessage(ColorMap)
_sym_db.RegisterMessage(ColorMap.LabelToColorEntry)


_COLORMAP_LABELTOCOLORENTRY._options = None
# @@protoc_insertion_point(module_scope)
