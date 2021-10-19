# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ibc.core.client.v1 import (
    client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="ibc/core/client/v1/tx.proto",
    package="ibc.core.client.v1",
    syntax="proto3",
    serialized_options=b"Z5github.com/cosmos/ibc-go/modules/core/02-client/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bibc/core/client/v1/tx.proto\x12\x12ibc.core.client.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1fibc/core/client/v1/client.proto"\xbb\x01\n\x0fMsgCreateClient\x12\x43\n\x0c\x63lient_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12I\n\x0f\x63onsensus_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:"consensus_state"\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x19\n\x17MsgCreateClientResponse"z\n\x0fMsgUpdateClient\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12$\n\x06header\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x19\n\x17MsgUpdateClientResponse"\xf5\x02\n\x10MsgUpgradeClient\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12\x43\n\x0c\x63lient_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12I\n\x0f\x63onsensus_state\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:"consensus_state"\x12=\n\x14proof_upgrade_client\x18\x04 \x01(\x0c\x42\x1f\xf2\xde\x1f\x1byaml:"proof_upgrade_client"\x12O\n\x1dproof_upgrade_consensus_state\x18\x05 \x01(\x0c\x42(\xf2\xde\x1f$yaml:"proof_upgrade_consensus_state"\x12\x0e\n\x06signer\x18\x06 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1a\n\x18MsgUpgradeClientResponse"\x86\x01\n\x15MsgSubmitMisbehaviour\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12*\n\x0cmisbehaviour\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x1f\n\x1dMsgSubmitMisbehaviourResponse2\xa2\x03\n\x03Msg\x12`\n\x0c\x43reateClient\x12#.ibc.core.client.v1.MsgCreateClient\x1a+.ibc.core.client.v1.MsgCreateClientResponse\x12`\n\x0cUpdateClient\x12#.ibc.core.client.v1.MsgUpdateClient\x1a+.ibc.core.client.v1.MsgUpdateClientResponse\x12\x63\n\rUpgradeClient\x12$.ibc.core.client.v1.MsgUpgradeClient\x1a,.ibc.core.client.v1.MsgUpgradeClientResponse\x12r\n\x12SubmitMisbehaviour\x12).ibc.core.client.v1.MsgSubmitMisbehaviour\x1a\x31.ibc.core.client.v1.MsgSubmitMisbehaviourResponseB7Z5github.com/cosmos/ibc-go/modules/core/02-client/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        ibc_dot_core_dot_client_dot_v1_dot_client__pb2.DESCRIPTOR,
    ],
)


_MSGCREATECLIENT = _descriptor.Descriptor(
    name="MsgCreateClient",
    full_name="ibc.core.client.v1.MsgCreateClient",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_state",
            full_name="ibc.core.client.v1.MsgCreateClient.client_state",
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
            serialized_options=b'\362\336\037\023yaml:"client_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="consensus_state",
            full_name="ibc.core.client.v1.MsgCreateClient.consensus_state",
            index=1,
            number=2,
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
            serialized_options=b'\362\336\037\026yaml:"consensus_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signer",
            full_name="ibc.core.client.v1.MsgCreateClient.signer",
            index=2,
            number=3,
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
    serialized_start=134,
    serialized_end=321,
)


_MSGCREATECLIENTRESPONSE = _descriptor.Descriptor(
    name="MsgCreateClientResponse",
    full_name="ibc.core.client.v1.MsgCreateClientResponse",
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
    serialized_start=323,
    serialized_end=348,
)


_MSGUPDATECLIENT = _descriptor.Descriptor(
    name="MsgUpdateClient",
    full_name="ibc.core.client.v1.MsgUpdateClient",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.MsgUpdateClient.client_id",
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
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="header",
            full_name="ibc.core.client.v1.MsgUpdateClient.header",
            index=1,
            number=2,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signer",
            full_name="ibc.core.client.v1.MsgUpdateClient.signer",
            index=2,
            number=3,
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
    serialized_start=350,
    serialized_end=472,
)


_MSGUPDATECLIENTRESPONSE = _descriptor.Descriptor(
    name="MsgUpdateClientResponse",
    full_name="ibc.core.client.v1.MsgUpdateClientResponse",
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
    serialized_start=474,
    serialized_end=499,
)


_MSGUPGRADECLIENT = _descriptor.Descriptor(
    name="MsgUpgradeClient",
    full_name="ibc.core.client.v1.MsgUpgradeClient",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.MsgUpgradeClient.client_id",
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
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="client_state",
            full_name="ibc.core.client.v1.MsgUpgradeClient.client_state",
            index=1,
            number=2,
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
            serialized_options=b'\362\336\037\023yaml:"client_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="consensus_state",
            full_name="ibc.core.client.v1.MsgUpgradeClient.consensus_state",
            index=2,
            number=3,
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
            serialized_options=b'\362\336\037\026yaml:"consensus_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proof_upgrade_client",
            full_name="ibc.core.client.v1.MsgUpgradeClient.proof_upgrade_client",
            index=3,
            number=4,
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
            serialized_options=b'\362\336\037\033yaml:"proof_upgrade_client"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proof_upgrade_consensus_state",
            full_name="ibc.core.client.v1.MsgUpgradeClient.proof_upgrade_consensus_state",
            index=4,
            number=5,
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
            serialized_options=b'\362\336\037$yaml:"proof_upgrade_consensus_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signer",
            full_name="ibc.core.client.v1.MsgUpgradeClient.signer",
            index=5,
            number=6,
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
    serialized_start=502,
    serialized_end=875,
)


_MSGUPGRADECLIENTRESPONSE = _descriptor.Descriptor(
    name="MsgUpgradeClientResponse",
    full_name="ibc.core.client.v1.MsgUpgradeClientResponse",
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
    serialized_start=877,
    serialized_end=903,
)


_MSGSUBMITMISBEHAVIOUR = _descriptor.Descriptor(
    name="MsgSubmitMisbehaviour",
    full_name="ibc.core.client.v1.MsgSubmitMisbehaviour",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.MsgSubmitMisbehaviour.client_id",
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
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="misbehaviour",
            full_name="ibc.core.client.v1.MsgSubmitMisbehaviour.misbehaviour",
            index=1,
            number=2,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signer",
            full_name="ibc.core.client.v1.MsgSubmitMisbehaviour.signer",
            index=2,
            number=3,
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
    serialized_start=906,
    serialized_end=1040,
)


_MSGSUBMITMISBEHAVIOURRESPONSE = _descriptor.Descriptor(
    name="MsgSubmitMisbehaviourResponse",
    full_name="ibc.core.client.v1.MsgSubmitMisbehaviourResponse",
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
    serialized_start=1042,
    serialized_end=1073,
)

_MSGCREATECLIENT.fields_by_name[
    "client_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGCREATECLIENT.fields_by_name[
    "consensus_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGUPDATECLIENT.fields_by_name[
    "header"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGUPGRADECLIENT.fields_by_name[
    "client_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGUPGRADECLIENT.fields_by_name[
    "consensus_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MSGSUBMITMISBEHAVIOUR.fields_by_name[
    "misbehaviour"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name["MsgCreateClient"] = _MSGCREATECLIENT
DESCRIPTOR.message_types_by_name["MsgCreateClientResponse"] = _MSGCREATECLIENTRESPONSE
DESCRIPTOR.message_types_by_name["MsgUpdateClient"] = _MSGUPDATECLIENT
DESCRIPTOR.message_types_by_name["MsgUpdateClientResponse"] = _MSGUPDATECLIENTRESPONSE
DESCRIPTOR.message_types_by_name["MsgUpgradeClient"] = _MSGUPGRADECLIENT
DESCRIPTOR.message_types_by_name["MsgUpgradeClientResponse"] = _MSGUPGRADECLIENTRESPONSE
DESCRIPTOR.message_types_by_name["MsgSubmitMisbehaviour"] = _MSGSUBMITMISBEHAVIOUR
DESCRIPTOR.message_types_by_name[
    "MsgSubmitMisbehaviourResponse"
] = _MSGSUBMITMISBEHAVIOURRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgCreateClient = _reflection.GeneratedProtocolMessageType(
    "MsgCreateClient",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGCREATECLIENT,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgCreateClient)
    },
)
_sym_db.RegisterMessage(MsgCreateClient)

MsgCreateClientResponse = _reflection.GeneratedProtocolMessageType(
    "MsgCreateClientResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGCREATECLIENTRESPONSE,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgCreateClientResponse)
    },
)
_sym_db.RegisterMessage(MsgCreateClientResponse)

MsgUpdateClient = _reflection.GeneratedProtocolMessageType(
    "MsgUpdateClient",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGUPDATECLIENT,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgUpdateClient)
    },
)
_sym_db.RegisterMessage(MsgUpdateClient)

MsgUpdateClientResponse = _reflection.GeneratedProtocolMessageType(
    "MsgUpdateClientResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGUPDATECLIENTRESPONSE,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgUpdateClientResponse)
    },
)
_sym_db.RegisterMessage(MsgUpdateClientResponse)

MsgUpgradeClient = _reflection.GeneratedProtocolMessageType(
    "MsgUpgradeClient",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGUPGRADECLIENT,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgUpgradeClient)
    },
)
_sym_db.RegisterMessage(MsgUpgradeClient)

MsgUpgradeClientResponse = _reflection.GeneratedProtocolMessageType(
    "MsgUpgradeClientResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGUPGRADECLIENTRESPONSE,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgUpgradeClientResponse)
    },
)
_sym_db.RegisterMessage(MsgUpgradeClientResponse)

MsgSubmitMisbehaviour = _reflection.GeneratedProtocolMessageType(
    "MsgSubmitMisbehaviour",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSUBMITMISBEHAVIOUR,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgSubmitMisbehaviour)
    },
)
_sym_db.RegisterMessage(MsgSubmitMisbehaviour)

MsgSubmitMisbehaviourResponse = _reflection.GeneratedProtocolMessageType(
    "MsgSubmitMisbehaviourResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGSUBMITMISBEHAVIOURRESPONSE,
        "__module__": "ibc.core.client.v1.tx_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.MsgSubmitMisbehaviourResponse)
    },
)
_sym_db.RegisterMessage(MsgSubmitMisbehaviourResponse)


DESCRIPTOR._options = None
_MSGCREATECLIENT.fields_by_name["client_state"]._options = None
_MSGCREATECLIENT.fields_by_name["consensus_state"]._options = None
_MSGCREATECLIENT._options = None
_MSGUPDATECLIENT.fields_by_name["client_id"]._options = None
_MSGUPDATECLIENT._options = None
_MSGUPGRADECLIENT.fields_by_name["client_id"]._options = None
_MSGUPGRADECLIENT.fields_by_name["client_state"]._options = None
_MSGUPGRADECLIENT.fields_by_name["consensus_state"]._options = None
_MSGUPGRADECLIENT.fields_by_name["proof_upgrade_client"]._options = None
_MSGUPGRADECLIENT.fields_by_name["proof_upgrade_consensus_state"]._options = None
_MSGUPGRADECLIENT._options = None
_MSGSUBMITMISBEHAVIOUR.fields_by_name["client_id"]._options = None
_MSGSUBMITMISBEHAVIOUR._options = None

_MSG = _descriptor.ServiceDescriptor(
    name="Msg",
    full_name="ibc.core.client.v1.Msg",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1076,
    serialized_end=1494,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateClient",
            full_name="ibc.core.client.v1.Msg.CreateClient",
            index=0,
            containing_service=None,
            input_type=_MSGCREATECLIENT,
            output_type=_MSGCREATECLIENTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateClient",
            full_name="ibc.core.client.v1.Msg.UpdateClient",
            index=1,
            containing_service=None,
            input_type=_MSGUPDATECLIENT,
            output_type=_MSGUPDATECLIENTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpgradeClient",
            full_name="ibc.core.client.v1.Msg.UpgradeClient",
            index=2,
            containing_service=None,
            input_type=_MSGUPGRADECLIENT,
            output_type=_MSGUPGRADECLIENTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SubmitMisbehaviour",
            full_name="ibc.core.client.v1.Msg.SubmitMisbehaviour",
            index=3,
            containing_service=None,
            input_type=_MSGSUBMITMISBEHAVIOUR,
            output_type=_MSGSUBMITMISBEHAVIOURRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name["Msg"] = _MSG

# @@protoc_insertion_point(module_scope)
