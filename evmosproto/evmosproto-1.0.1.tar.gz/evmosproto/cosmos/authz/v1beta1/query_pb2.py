# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmosproto.cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/authz/v1beta1/query.proto',
  package='cosmos.authz.v1beta1',
  syntax='proto3',
  serialized_options=b'Z$github.com/cosmos/cosmos-sdk/x/authz',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cosmos/authz/v1beta1/query.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a cosmos/authz/v1beta1/authz.proto\"\x88\x01\n\x12QueryGrantsRequest\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t\x12:\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x7f\n\x13QueryGrantsResponse\x12+\n\x06grants\x18\x01 \x03(\x0b\x32\x1b.cosmos.authz.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x8d\x01\n\x05Query\x12\x83\x01\n\x06Grants\x12(.cosmos.authz.v1beta1.QueryGrantsRequest\x1a).cosmos.authz.v1beta1.QueryGrantsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/authz/v1beta1/grantsB&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,cosmos_dot_authz_dot_v1beta1_dot_authz__pb2.DESCRIPTOR,])




_QUERYGRANTSREQUEST = _descriptor.Descriptor(
  name='QueryGrantsRequest',
  full_name='cosmos.authz.v1beta1.QueryGrantsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.authz.v1beta1.QueryGrantsRequest.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.authz.v1beta1.QueryGrantsRequest.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_type_url', full_name='cosmos.authz.v1beta1.QueryGrantsRequest.msg_type_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.authz.v1beta1.QueryGrantsRequest.pagination', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=303,
)


_QUERYGRANTSRESPONSE = _descriptor.Descriptor(
  name='QueryGrantsResponse',
  full_name='cosmos.authz.v1beta1.QueryGrantsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grants', full_name='cosmos.authz.v1beta1.QueryGrantsResponse.grants', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.authz.v1beta1.QueryGrantsResponse.pagination', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=432,
)

_QUERYGRANTSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYGRANTSRESPONSE.fields_by_name['grants'].message_type = cosmos_dot_authz_dot_v1beta1_dot_authz__pb2._GRANT
_QUERYGRANTSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
DESCRIPTOR.message_types_by_name['QueryGrantsRequest'] = _QUERYGRANTSREQUEST
DESCRIPTOR.message_types_by_name['QueryGrantsResponse'] = _QUERYGRANTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryGrantsRequest = _reflection.GeneratedProtocolMessageType('QueryGrantsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTSREQUEST,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGrantsRequest)
  })
_sym_db.RegisterMessage(QueryGrantsRequest)

QueryGrantsResponse = _reflection.GeneratedProtocolMessageType('QueryGrantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYGRANTSRESPONSE,
  '__module__' : 'cosmos.authz.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.authz.v1beta1.QueryGrantsResponse)
  })
_sym_db.RegisterMessage(QueryGrantsResponse)


DESCRIPTOR._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.authz.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=435,
  serialized_end=576,
  methods=[
  _descriptor.MethodDescriptor(
    name='Grants',
    full_name='cosmos.authz.v1beta1.Query.Grants',
    index=0,
    containing_service=None,
    input_type=_QUERYGRANTSREQUEST,
    output_type=_QUERYGRANTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/cosmos/authz/v1beta1/grants',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
