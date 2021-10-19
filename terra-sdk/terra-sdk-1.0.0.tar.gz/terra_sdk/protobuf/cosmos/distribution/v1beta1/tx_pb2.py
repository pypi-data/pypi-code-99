# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/distribution/v1beta1/tx.proto",
    package="cosmos.distribution.v1beta1",
    syntax="proto3",
    serialized_options=b"Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n$cosmos/distribution/v1beta1/tx.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\x91\x01\n\x15MsgSetWithdrawAddress\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x12\x35\n\x10withdraw_address\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"withdraw_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1f\n\x1dMsgSetWithdrawAddressResponse"\x98\x01\n\x1aMsgWithdrawDelegatorReward\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x12\x37\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"$\n"MsgWithdrawDelegatorRewardResponse"c\n\x1eMsgWithdrawValidatorCommission\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"(\n&MsgWithdrawValidatorCommissionResponse"\x90\x01\n\x14MsgFundCommunityPool\x12[\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x11\n\tdepositor\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1e\n\x1cMsgFundCommunityPoolResponse2\xc8\x04\n\x03Msg\x12\x84\x01\n\x12SetWithdrawAddress\x12\x32.cosmos.distribution.v1beta1.MsgSetWithdrawAddress\x1a:.cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse\x12\x93\x01\n\x17WithdrawDelegatorReward\x12\x37.cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward\x1a?.cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse\x12\x9f\x01\n\x1bWithdrawValidatorCommission\x12;.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission\x1a\x43.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse\x12\x81\x01\n\x11\x46undCommunityPool\x12\x31.cosmos.distribution.v1beta1.MsgFundCommunityPool\x1a\x39.cosmos.distribution.v1beta1.MsgFundCommunityPoolResponseB7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
    ],
)


_MSGSETWITHDRAWADDRESS = _descriptor.Descriptor(
    name="MsgSetWithdrawAddress",
    full_name="cosmos.distribution.v1beta1.MsgSetWithdrawAddress",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="delegator_address",
            full_name="cosmos.distribution.v1beta1.MsgSetWithdrawAddress.delegator_address",
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
            serialized_options=b'\362\336\037\030yaml:"delegator_address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="withdraw_address",
            full_name="cosmos.distribution.v1beta1.MsgSetWithdrawAddress.withdraw_address",
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
            serialized_options=b'\362\336\037\027yaml:"withdraw_address"',
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
    serialized_start=124,
    serialized_end=269,
)


_MSGSETWITHDRAWADDRESSRESPONSE = _descriptor.Descriptor(
    name="MsgSetWithdrawAddressResponse",
    full_name="cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse",
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
    serialized_start=271,
    serialized_end=302,
)


_MSGWITHDRAWDELEGATORREWARD = _descriptor.Descriptor(
    name="MsgWithdrawDelegatorReward",
    full_name="cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="delegator_address",
            full_name="cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward.delegator_address",
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
            serialized_options=b'\362\336\037\030yaml:"delegator_address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="validator_address",
            full_name="cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward.validator_address",
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
            serialized_options=b'\362\336\037\030yaml:"validator_address"',
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
    serialized_start=305,
    serialized_end=457,
)


_MSGWITHDRAWDELEGATORREWARDRESPONSE = _descriptor.Descriptor(
    name="MsgWithdrawDelegatorRewardResponse",
    full_name="cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse",
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
    serialized_start=459,
    serialized_end=495,
)


_MSGWITHDRAWVALIDATORCOMMISSION = _descriptor.Descriptor(
    name="MsgWithdrawValidatorCommission",
    full_name="cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="validator_address",
            full_name="cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission.validator_address",
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
            serialized_options=b'\362\336\037\030yaml:"validator_address"',
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
    serialized_start=497,
    serialized_end=596,
)


_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE = _descriptor.Descriptor(
    name="MsgWithdrawValidatorCommissionResponse",
    full_name="cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse",
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
    serialized_start=598,
    serialized_end=638,
)


_MSGFUNDCOMMUNITYPOOL = _descriptor.Descriptor(
    name="MsgFundCommunityPool",
    full_name="cosmos.distribution.v1beta1.MsgFundCommunityPool",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="cosmos.distribution.v1beta1.MsgFundCommunityPool.amount",
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
        _descriptor.FieldDescriptor(
            name="depositor",
            full_name="cosmos.distribution.v1beta1.MsgFundCommunityPool.depositor",
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
    serialized_start=641,
    serialized_end=785,
)


_MSGFUNDCOMMUNITYPOOLRESPONSE = _descriptor.Descriptor(
    name="MsgFundCommunityPoolResponse",
    full_name="cosmos.distribution.v1beta1.MsgFundCommunityPoolResponse",
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
    serialized_start=787,
    serialized_end=817,
)

_MSGFUNDCOMMUNITYPOOL.fields_by_name[
    "amount"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name["MsgSetWithdrawAddress"] = _MSGSETWITHDRAWADDRESS
DESCRIPTOR.message_types_by_name[
    "MsgSetWithdrawAddressResponse"
] = _MSGSETWITHDRAWADDRESSRESPONSE
DESCRIPTOR.message_types_by_name[
    "MsgWithdrawDelegatorReward"
] = _MSGWITHDRAWDELEGATORREWARD
DESCRIPTOR.message_types_by_name[
    "MsgWithdrawDelegatorRewardResponse"
] = _MSGWITHDRAWDELEGATORREWARDRESPONSE
DESCRIPTOR.message_types_by_name[
    "MsgWithdrawValidatorCommission"
] = _MSGWITHDRAWVALIDATORCOMMISSION
DESCRIPTOR.message_types_by_name[
    "MsgWithdrawValidatorCommissionResponse"
] = _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE
DESCRIPTOR.message_types_by_name["MsgFundCommunityPool"] = _MSGFUNDCOMMUNITYPOOL
DESCRIPTOR.message_types_by_name[
    "MsgFundCommunityPoolResponse"
] = _MSGFUNDCOMMUNITYPOOLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgSetWithdrawAddress = _reflection.GeneratedProtocolMessageType(
    "MsgSetWithdrawAddress",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSETWITHDRAWADDRESS,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgSetWithdrawAddress)
    },
)
_sym_db.RegisterMessage(MsgSetWithdrawAddress)

MsgSetWithdrawAddressResponse = _reflection.GeneratedProtocolMessageType(
    "MsgSetWithdrawAddressResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSETWITHDRAWADDRESSRESPONSE,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse)
    },
)
_sym_db.RegisterMessage(MsgSetWithdrawAddressResponse)

MsgWithdrawDelegatorReward = _reflection.GeneratedProtocolMessageType(
    "MsgWithdrawDelegatorReward",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGWITHDRAWDELEGATORREWARD,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward)
    },
)
_sym_db.RegisterMessage(MsgWithdrawDelegatorReward)

MsgWithdrawDelegatorRewardResponse = _reflection.GeneratedProtocolMessageType(
    "MsgWithdrawDelegatorRewardResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGWITHDRAWDELEGATORREWARDRESPONSE,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse)
    },
)
_sym_db.RegisterMessage(MsgWithdrawDelegatorRewardResponse)

MsgWithdrawValidatorCommission = _reflection.GeneratedProtocolMessageType(
    "MsgWithdrawValidatorCommission",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGWITHDRAWVALIDATORCOMMISSION,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission)
    },
)
_sym_db.RegisterMessage(MsgWithdrawValidatorCommission)

MsgWithdrawValidatorCommissionResponse = _reflection.GeneratedProtocolMessageType(
    "MsgWithdrawValidatorCommissionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse)
    },
)
_sym_db.RegisterMessage(MsgWithdrawValidatorCommissionResponse)

MsgFundCommunityPool = _reflection.GeneratedProtocolMessageType(
    "MsgFundCommunityPool",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGFUNDCOMMUNITYPOOL,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgFundCommunityPool)
    },
)
_sym_db.RegisterMessage(MsgFundCommunityPool)

MsgFundCommunityPoolResponse = _reflection.GeneratedProtocolMessageType(
    "MsgFundCommunityPoolResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGFUNDCOMMUNITYPOOLRESPONSE,
        "__module__": "cosmos.distribution.v1beta1.tx_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.MsgFundCommunityPoolResponse)
    },
)
_sym_db.RegisterMessage(MsgFundCommunityPoolResponse)


DESCRIPTOR._options = None
_MSGSETWITHDRAWADDRESS.fields_by_name["delegator_address"]._options = None
_MSGSETWITHDRAWADDRESS.fields_by_name["withdraw_address"]._options = None
_MSGSETWITHDRAWADDRESS._options = None
_MSGWITHDRAWDELEGATORREWARD.fields_by_name["delegator_address"]._options = None
_MSGWITHDRAWDELEGATORREWARD.fields_by_name["validator_address"]._options = None
_MSGWITHDRAWDELEGATORREWARD._options = None
_MSGWITHDRAWVALIDATORCOMMISSION.fields_by_name["validator_address"]._options = None
_MSGWITHDRAWVALIDATORCOMMISSION._options = None
_MSGFUNDCOMMUNITYPOOL.fields_by_name["amount"]._options = None
_MSGFUNDCOMMUNITYPOOL._options = None

_MSG = _descriptor.ServiceDescriptor(
    name="Msg",
    full_name="cosmos.distribution.v1beta1.Msg",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=820,
    serialized_end=1404,
    methods=[
        _descriptor.MethodDescriptor(
            name="SetWithdrawAddress",
            full_name="cosmos.distribution.v1beta1.Msg.SetWithdrawAddress",
            index=0,
            containing_service=None,
            input_type=_MSGSETWITHDRAWADDRESS,
            output_type=_MSGSETWITHDRAWADDRESSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="WithdrawDelegatorReward",
            full_name="cosmos.distribution.v1beta1.Msg.WithdrawDelegatorReward",
            index=1,
            containing_service=None,
            input_type=_MSGWITHDRAWDELEGATORREWARD,
            output_type=_MSGWITHDRAWDELEGATORREWARDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="WithdrawValidatorCommission",
            full_name="cosmos.distribution.v1beta1.Msg.WithdrawValidatorCommission",
            index=2,
            containing_service=None,
            input_type=_MSGWITHDRAWVALIDATORCOMMISSION,
            output_type=_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="FundCommunityPool",
            full_name="cosmos.distribution.v1beta1.Msg.FundCommunityPool",
            index=3,
            containing_service=None,
            input_type=_MSGFUNDCOMMUNITYPOOL,
            output_type=_MSGFUNDCOMMUNITYPOOLRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name["Msg"] = _MSG

# @@protoc_insertion_point(module_scope)
