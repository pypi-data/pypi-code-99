# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/kv/v1beta1/kv.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/kv/v1beta1/kv.proto',
  package='cosmos.base.kv.v1beta1',
  syntax='proto3',
  serialized_options=b'Z%github.com/cosmos/cosmos-sdk/types/kv',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63osmos/base/kv/v1beta1/kv.proto\x12\x16\x63osmos.base.kv.v1beta1\x1a\x14gogoproto/gogo.proto\":\n\x05Pairs\x12\x31\n\x05pairs\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.kv.v1beta1.PairB\x04\xc8\xde\x1f\x00\"\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x42\'Z%github.com/cosmos/cosmos-sdk/types/kvb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PAIRS = _descriptor.Descriptor(
  name='Pairs',
  full_name='cosmos.base.kv.v1beta1.Pairs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pairs', full_name='cosmos.base.kv.v1beta1.Pairs.pairs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=81,
  serialized_end=139,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='cosmos.base.kv.v1beta1.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.base.kv.v1beta1.Pair.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cosmos.base.kv.v1beta1.Pair.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=141,
  serialized_end=175,
)

_PAIRS.fields_by_name['pairs'].message_type = _PAIR
DESCRIPTOR.message_types_by_name['Pairs'] = _PAIRS
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pairs = _reflection.GeneratedProtocolMessageType('Pairs', (_message.Message,), {
  'DESCRIPTOR' : _PAIRS,
  '__module__' : 'cosmos.base.kv.v1beta1.kv_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.kv.v1beta1.Pairs)
  })
_sym_db.RegisterMessage(Pairs)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'cosmos.base.kv.v1beta1.kv_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.kv.v1beta1.Pair)
  })
_sym_db.RegisterMessage(Pair)


DESCRIPTOR._options = None
_PAIRS.fields_by_name['pairs']._options = None
# @@protoc_insertion_point(module_scope)
