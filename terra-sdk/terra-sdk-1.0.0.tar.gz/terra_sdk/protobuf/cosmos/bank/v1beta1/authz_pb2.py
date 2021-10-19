# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/bank/v1beta1/authz.proto",
    package="cosmos.bank.v1beta1",
    syntax="proto3",
    serialized_options=b"Z)github.com/cosmos/cosmos-sdk/x/bank/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1f\x63osmos/bank/v1beta1/authz.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\x88\x01\n\x11SendAuthorization\x12`\n\x0bspend_limit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x11\xd2\xb4-\rAuthorizationB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
    ],
)


_SENDAUTHORIZATION = _descriptor.Descriptor(
    name="SendAuthorization",
    full_name="cosmos.bank.v1beta1.SendAuthorization",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="spend_limit",
            full_name="cosmos.bank.v1beta1.SendAuthorization.spend_limit",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\322\264-\rAuthorization",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=138,
    serialized_end=274,
)

_SENDAUTHORIZATION.fields_by_name[
    "spend_limit"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name["SendAuthorization"] = _SENDAUTHORIZATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendAuthorization = _reflection.GeneratedProtocolMessageType(
    "SendAuthorization",
    (_message.Message,),
    {
        "DESCRIPTOR": _SENDAUTHORIZATION,
        "__module__": "cosmos.bank.v1beta1.authz_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.SendAuthorization)
    },
)
_sym_db.RegisterMessage(SendAuthorization)


DESCRIPTOR._options = None
_SENDAUTHORIZATION.fields_by_name["spend_limit"]._options = None
_SENDAUTHORIZATION._options = None
# @@protoc_insertion_point(module_scope)
