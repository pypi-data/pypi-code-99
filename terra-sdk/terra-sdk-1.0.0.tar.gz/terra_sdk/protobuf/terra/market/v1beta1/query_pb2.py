# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terra/market/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from terra.market.v1beta1 import (
    market_pb2 as terra_dot_market_dot_v1beta1_dot_market__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="terra/market/v1beta1/query.proto",
    package="terra.market.v1beta1",
    syntax="proto3",
    serialized_options=b"Z*github.com/terra-money/core/x/market/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n terra/market/v1beta1/query.proto\x12\x14terra.market.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!terra/market/v1beta1/market.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"C\n\x10QuerySwapRequest\x12\x12\n\noffer_coin\x18\x01 \x01(\t\x12\x11\n\task_denom\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"I\n\x11QuerySwapResponse\x12\x34\n\x0breturn_coin\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x1c\n\x1aQueryTerraPoolDeltaRequest"g\n\x1bQueryTerraPoolDeltaResponse\x12H\n\x10terra_pool_delta\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"I\n\x13QueryParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1c.terra.market.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x32\xb2\x03\n\x05Query\x12{\n\x04Swap\x12&.terra.market.v1beta1.QuerySwapRequest\x1a\'.terra.market.v1beta1.QuerySwapResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/terra/market/v1beta1/swap\x12\xa5\x01\n\x0eTerraPoolDelta\x12\x30.terra.market.v1beta1.QueryTerraPoolDeltaRequest\x1a\x31.terra.market.v1beta1.QueryTerraPoolDeltaResponse".\x82\xd3\xe4\x93\x02(\x12&/terra/market/v1beta1/terra_pool_delta\x12\x83\x01\n\x06Params\x12(.terra.market.v1beta1.QueryParamsRequest\x1a).terra.market.v1beta1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/terra/market/v1beta1/paramsB,Z*github.com/terra-money/core/x/market/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        terra_dot_market_dot_v1beta1_dot_market__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
    ],
)


_QUERYSWAPREQUEST = _descriptor.Descriptor(
    name="QuerySwapRequest",
    full_name="terra.market.v1beta1.QuerySwapRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="offer_coin",
            full_name="terra.market.v1beta1.QuerySwapRequest.offer_coin",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ask_denom",
            full_name="terra.market.v1beta1.QuerySwapRequest.ask_denom",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\000\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=177,
    serialized_end=244,
)


_QUERYSWAPRESPONSE = _descriptor.Descriptor(
    name="QuerySwapResponse",
    full_name="terra.market.v1beta1.QuerySwapResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="return_coin",
            full_name="terra.market.v1beta1.QuerySwapResponse.return_coin",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=246,
    serialized_end=319,
)


_QUERYTERRAPOOLDELTAREQUEST = _descriptor.Descriptor(
    name="QueryTerraPoolDeltaRequest",
    full_name="terra.market.v1beta1.QueryTerraPoolDeltaRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=321,
    serialized_end=349,
)


_QUERYTERRAPOOLDELTARESPONSE = _descriptor.Descriptor(
    name="QueryTerraPoolDeltaResponse",
    full_name="terra.market.v1beta1.QueryTerraPoolDeltaResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="terra_pool_delta",
            full_name="terra.market.v1beta1.QueryTerraPoolDeltaResponse.terra_pool_delta",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=351,
    serialized_end=454,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
    name="QueryParamsRequest",
    full_name="terra.market.v1beta1.QueryParamsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=456,
    serialized_end=476,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
    name="QueryParamsResponse",
    full_name="terra.market.v1beta1.QueryParamsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="params",
            full_name="terra.market.v1beta1.QueryParamsResponse.params",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=478,
    serialized_end=551,
)

_QUERYSWAPRESPONSE.fields_by_name[
    "return_coin"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYPARAMSRESPONSE.fields_by_name[
    "params"
].message_type = terra_dot_market_dot_v1beta1_dot_market__pb2._PARAMS
DESCRIPTOR.message_types_by_name["QuerySwapRequest"] = _QUERYSWAPREQUEST
DESCRIPTOR.message_types_by_name["QuerySwapResponse"] = _QUERYSWAPRESPONSE
DESCRIPTOR.message_types_by_name[
    "QueryTerraPoolDeltaRequest"
] = _QUERYTERRAPOOLDELTAREQUEST
DESCRIPTOR.message_types_by_name[
    "QueryTerraPoolDeltaResponse"
] = _QUERYTERRAPOOLDELTARESPONSE
DESCRIPTOR.message_types_by_name["QueryParamsRequest"] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name["QueryParamsResponse"] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuerySwapRequest = _reflection.GeneratedProtocolMessageType(
    "QuerySwapRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYSWAPREQUEST,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QuerySwapRequest)
    },
)
_sym_db.RegisterMessage(QuerySwapRequest)

QuerySwapResponse = _reflection.GeneratedProtocolMessageType(
    "QuerySwapResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYSWAPRESPONSE,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QuerySwapResponse)
    },
)
_sym_db.RegisterMessage(QuerySwapResponse)

QueryTerraPoolDeltaRequest = _reflection.GeneratedProtocolMessageType(
    "QueryTerraPoolDeltaRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYTERRAPOOLDELTAREQUEST,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QueryTerraPoolDeltaRequest)
    },
)
_sym_db.RegisterMessage(QueryTerraPoolDeltaRequest)

QueryTerraPoolDeltaResponse = _reflection.GeneratedProtocolMessageType(
    "QueryTerraPoolDeltaResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYTERRAPOOLDELTARESPONSE,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QueryTerraPoolDeltaResponse)
    },
)
_sym_db.RegisterMessage(QueryTerraPoolDeltaResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType(
    "QueryParamsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSREQUEST,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QueryParamsRequest)
    },
)
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType(
    "QueryParamsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSRESPONSE,
        "__module__": "terra.market.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:terra.market.v1beta1.QueryParamsResponse)
    },
)
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYSWAPREQUEST._options = None
_QUERYSWAPRESPONSE.fields_by_name["return_coin"]._options = None
_QUERYTERRAPOOLDELTARESPONSE.fields_by_name["terra_pool_delta"]._options = None
_QUERYPARAMSRESPONSE.fields_by_name["params"]._options = None

_QUERY = _descriptor.ServiceDescriptor(
    name="Query",
    full_name="terra.market.v1beta1.Query",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=554,
    serialized_end=988,
    methods=[
        _descriptor.MethodDescriptor(
            name="Swap",
            full_name="terra.market.v1beta1.Query.Swap",
            index=0,
            containing_service=None,
            input_type=_QUERYSWAPREQUEST,
            output_type=_QUERYSWAPRESPONSE,
            serialized_options=b"\202\323\344\223\002\034\022\032/terra/market/v1beta1/swap",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="TerraPoolDelta",
            full_name="terra.market.v1beta1.Query.TerraPoolDelta",
            index=1,
            containing_service=None,
            input_type=_QUERYTERRAPOOLDELTAREQUEST,
            output_type=_QUERYTERRAPOOLDELTARESPONSE,
            serialized_options=b"\202\323\344\223\002(\022&/terra/market/v1beta1/terra_pool_delta",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Params",
            full_name="terra.market.v1beta1.Query.Params",
            index=2,
            containing_service=None,
            input_type=_QUERYPARAMSREQUEST,
            output_type=_QUERYPARAMSRESPONSE,
            serialized_options=b"\202\323\344\223\002\036\022\034/terra/market/v1beta1/params",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name["Query"] = _QUERY

# @@protoc_insertion_point(module_scope)
