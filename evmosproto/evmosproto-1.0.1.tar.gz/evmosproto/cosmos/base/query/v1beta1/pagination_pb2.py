# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/query/v1beta1/pagination.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/query/v1beta1/pagination.proto',
  package='cosmos.base.query.v1beta1',
  syntax='proto3',
  serialized_options=b'Z(github.com/cosmos/cosmos-sdk/types/query',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*cosmos/base/query/v1beta1/pagination.proto\x12\x19\x63osmos.base.query.v1beta1\"_\n\x0bPageRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\r\n\x05limit\x18\x03 \x01(\x04\x12\x13\n\x0b\x63ount_total\x18\x04 \x01(\x08\x12\x0f\n\x07reverse\x18\x05 \x01(\x08\"/\n\x0cPageResponse\x12\x10\n\x08next_key\x18\x01 \x01(\x0c\x12\r\n\x05total\x18\x02 \x01(\x04\x42*Z(github.com/cosmos/cosmos-sdk/types/queryb\x06proto3'
)




_PAGEREQUEST = _descriptor.Descriptor(
  name='PageRequest',
  full_name='cosmos.base.query.v1beta1.PageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.base.query.v1beta1.PageRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='cosmos.base.query.v1beta1.PageRequest.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='cosmos.base.query.v1beta1.PageRequest.limit', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count_total', full_name='cosmos.base.query.v1beta1.PageRequest.count_total', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='cosmos.base.query.v1beta1.PageRequest.reverse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=168,
)


_PAGERESPONSE = _descriptor.Descriptor(
  name='PageResponse',
  full_name='cosmos.base.query.v1beta1.PageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_key', full_name='cosmos.base.query.v1beta1.PageResponse.next_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='cosmos.base.query.v1beta1.PageResponse.total', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['PageRequest'] = _PAGEREQUEST
DESCRIPTOR.message_types_by_name['PageResponse'] = _PAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageRequest = _reflection.GeneratedProtocolMessageType('PageRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGEREQUEST,
  '__module__' : 'cosmos.base.query.v1beta1.pagination_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.query.v1beta1.PageRequest)
  })
_sym_db.RegisterMessage(PageRequest)

PageResponse = _reflection.GeneratedProtocolMessageType('PageResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAGERESPONSE,
  '__module__' : 'cosmos.base.query.v1beta1.pagination_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.query.v1beta1.PageResponse)
  })
_sym_db.RegisterMessage(PageResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
