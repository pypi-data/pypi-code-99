# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/distribution.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/distribution/v1beta1/distribution.proto',
  package='cosmos.distribution.v1beta1',
  syntax='proto3',
  serialized_options=b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.cosmos/distribution/v1beta1/distribution.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x8a\x03\n\x06Params\x12]\n\rcommunity_tax\x18\x01 \x01(\tBF\xf2\xde\x1f\x14yaml:\"community_tax\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12k\n\x14\x62\x61se_proposer_reward\x18\x02 \x01(\tBM\xf2\xde\x1f\x1byaml:\"base_proposer_reward\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12m\n\x15\x62onus_proposer_reward\x18\x03 \x01(\tBN\xf2\xde\x1f\x1cyaml:\"bonus_proposer_reward\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12?\n\x15withdraw_addr_enabled\x18\x04 \x01(\x08\x42 \xf2\xde\x1f\x1cyaml:\"withdraw_addr_enabled\":\x04\x98\xa0\x1f\x00\"\xe8\x01\n\x1aValidatorHistoricalRewards\x12\x94\x01\n\x17\x63umulative_reward_ratio\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBU\xf2\xde\x1f\x1eyaml:\"cumulative_reward_ratio\"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x33\n\x0freference_count\x18\x02 \x01(\rB\x1a\xf2\xde\x1f\x16yaml:\"reference_count\"\"\x8d\x01\n\x17ValidatorCurrentRewards\x12\x62\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\x12\x0e\n\x06period\x18\x02 \x01(\x04\"\x87\x01\n\x1eValidatorAccumulatedCommission\x12\x65\n\ncommission\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x93\x01\n\x1bValidatorOutstandingRewards\x12t\n\x07rewards\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBE\xf2\xde\x1f\x0eyaml:\"rewards\"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\"\x8e\x01\n\x13ValidatorSlashEvent\x12\x35\n\x10validator_period\x18\x01 \x01(\x04\x42\x1b\xf2\xde\x1f\x17yaml:\"validator_period\"\x12@\n\x08\x66raction\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x95\x01\n\x14ValidatorSlashEvents\x12w\n\x16validator_slash_events\x18\x01 \x03(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB%\xf2\xde\x1f\x1dyaml:\"validator_slash_events\"\xc8\xde\x1f\x00:\x04\x98\xa0\x1f\x00\"\x8e\x01\n\x07\x46\x65\x65Pool\x12\x82\x01\n\x0e\x63ommunity_pool\x18\x01 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinBL\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xf2\xde\x1f\x15yaml:\"community_pool\"\"\xbe\x01\n\x1a\x43ommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06\x61mount\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xda\x01\n\x15\x44\x65legatorStartingInfo\x12\x33\n\x0fprevious_period\x18\x01 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:\"previous_period\"\x12M\n\x05stake\x18\x02 \x01(\tB>\xf2\xde\x1f\x0cyaml:\"stake\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12=\n\x06height\x18\x03 \x01(\x04\x42-\xf2\xde\x1f\x16yaml:\"creation_height\"\xea\xde\x1f\x0f\x63reation_height\"\xc1\x01\n\x19\x44\x65legationDelegatorReward\x12\x37\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12\x61\n\x06reward\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\"\xf0\x01\n%CommunityPoolSpendProposalWithDeposit\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12\'\n\trecipient\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"recipient\"\x12!\n\x06\x61mount\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"amount\"\x12#\n\x07\x64\x65posit\x18\x05 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"deposit\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.distribution.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_tax', full_name='cosmos.distribution.v1beta1.Params.community_tax', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\024yaml:\"community_tax\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_proposer_reward', full_name='cosmos.distribution.v1beta1.Params.base_proposer_reward', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"base_proposer_reward\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bonus_proposer_reward', full_name='cosmos.distribution.v1beta1.Params.bonus_proposer_reward', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"bonus_proposer_reward\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='withdraw_addr_enabled', full_name='cosmos.distribution.v1beta1.Params.withdraw_addr_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"withdraw_addr_enabled\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=528,
)


_VALIDATORHISTORICALREWARDS = _descriptor.Descriptor(
  name='ValidatorHistoricalRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulative_reward_ratio', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards.cumulative_reward_ratio', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\036yaml:\"cumulative_reward_ratio\"\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewards.reference_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"reference_count\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=531,
  serialized_end=763,
)


_VALIDATORCURRENTREWARDS = _descriptor.Descriptor(
  name='ValidatorCurrentRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewards.period', index=1,
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
  serialized_start=766,
  serialized_end=907,
)


_VALIDATORACCUMULATEDCOMMISSION = _descriptor.Descriptor(
  name='ValidatorAccumulatedCommission',
  full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commission', full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommission.commission', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=910,
  serialized_end=1045,
)


_VALIDATOROUTSTANDINGREWARDS = _descriptor.Descriptor(
  name='ValidatorOutstandingRewards',
  full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"rewards\"\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1048,
  serialized_end=1195,
)


_VALIDATORSLASHEVENT = _descriptor.Descriptor(
  name='ValidatorSlashEvent',
  full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_period', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent.validator_period', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\027yaml:\"validator_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fraction', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvent.fraction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1198,
  serialized_end=1340,
)


_VALIDATORSLASHEVENTS = _descriptor.Descriptor(
  name='ValidatorSlashEvents',
  full_name='cosmos.distribution.v1beta1.ValidatorSlashEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_slash_events', full_name='cosmos.distribution.v1beta1.ValidatorSlashEvents.validator_slash_events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\035yaml:\"validator_slash_events\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1343,
  serialized_end=1492,
)


_FEEPOOL = _descriptor.Descriptor(
  name='FeePool',
  full_name='cosmos.distribution.v1beta1.FeePool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_pool', full_name='cosmos.distribution.v1beta1.FeePool.community_pool', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\362\336\037\025yaml:\"community_pool\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1495,
  serialized_end=1637,
)


_COMMUNITYPOOLSPENDPROPOSAL = _descriptor.Descriptor(
  name='CommunityPoolSpendProposal',
  full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.recipient', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposal.amount', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1640,
  serialized_end=1830,
)


_DELEGATORSTARTINGINFO = _descriptor.Descriptor(
  name='DelegatorStartingInfo',
  full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_period', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.previous_period', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"previous_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stake', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.stake', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\014yaml:\"stake\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfo.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"creation_height\"\352\336\037\017creation_height', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1833,
  serialized_end=2051,
)


_DELEGATIONDELEGATORREWARD = _descriptor.Descriptor(
  name='DelegationDelegatorReward',
  full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\030yaml:\"validator_address\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward', full_name='cosmos.distribution.v1beta1.DelegationDelegatorReward.reward', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2054,
  serialized_end=2247,
)


_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT = _descriptor.Descriptor(
  name='CommunityPoolSpendProposalWithDeposit',
  full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\014yaml:\"title\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\022yaml:\"description\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.recipient', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"recipient\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.amount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\ryaml:\"amount\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deposit', full_name='cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit.deposit', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"deposit\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2250,
  serialized_end=2490,
)

_VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORCURRENTREWARDS.fields_by_name['rewards'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events'].message_type = _VALIDATORSLASHEVENT
_FEEPOOL.fields_by_name['community_pool'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_DELEGATIONDELEGATORREWARD.fields_by_name['reward'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewards'] = _VALIDATORHISTORICALREWARDS
DESCRIPTOR.message_types_by_name['ValidatorCurrentRewards'] = _VALIDATORCURRENTREWARDS
DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommission'] = _VALIDATORACCUMULATEDCOMMISSION
DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewards'] = _VALIDATOROUTSTANDINGREWARDS
DESCRIPTOR.message_types_by_name['ValidatorSlashEvent'] = _VALIDATORSLASHEVENT
DESCRIPTOR.message_types_by_name['ValidatorSlashEvents'] = _VALIDATORSLASHEVENTS
DESCRIPTOR.message_types_by_name['FeePool'] = _FEEPOOL
DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposal'] = _COMMUNITYPOOLSPENDPROPOSAL
DESCRIPTOR.message_types_by_name['DelegatorStartingInfo'] = _DELEGATORSTARTINGINFO
DESCRIPTOR.message_types_by_name['DelegationDelegatorReward'] = _DELEGATIONDELEGATORREWARD
DESCRIPTOR.message_types_by_name['CommunityPoolSpendProposalWithDeposit'] = _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)

ValidatorHistoricalRewards = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewards', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORHISTORICALREWARDS,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorHistoricalRewards)
  })
_sym_db.RegisterMessage(ValidatorHistoricalRewards)

ValidatorCurrentRewards = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewards', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORCURRENTREWARDS,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorCurrentRewards)
  })
_sym_db.RegisterMessage(ValidatorCurrentRewards)

ValidatorAccumulatedCommission = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommission', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORACCUMULATEDCOMMISSION,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorAccumulatedCommission)
  })
_sym_db.RegisterMessage(ValidatorAccumulatedCommission)

ValidatorOutstandingRewards = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewards', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOROUTSTANDINGREWARDS,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorOutstandingRewards)
  })
_sym_db.RegisterMessage(ValidatorOutstandingRewards)

ValidatorSlashEvent = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvent', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSLASHEVENT,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvent)
  })
_sym_db.RegisterMessage(ValidatorSlashEvent)

ValidatorSlashEvents = _reflection.GeneratedProtocolMessageType('ValidatorSlashEvents', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSLASHEVENTS,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEvents)
  })
_sym_db.RegisterMessage(ValidatorSlashEvents)

FeePool = _reflection.GeneratedProtocolMessageType('FeePool', (_message.Message,), {
  'DESCRIPTOR' : _FEEPOOL,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.FeePool)
  })
_sym_db.RegisterMessage(FeePool)

CommunityPoolSpendProposal = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposal', (_message.Message,), {
  'DESCRIPTOR' : _COMMUNITYPOOLSPENDPROPOSAL,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposal)
  })
_sym_db.RegisterMessage(CommunityPoolSpendProposal)

DelegatorStartingInfo = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATORSTARTINGINFO,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorStartingInfo)
  })
_sym_db.RegisterMessage(DelegatorStartingInfo)

DelegationDelegatorReward = _reflection.GeneratedProtocolMessageType('DelegationDelegatorReward', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATIONDELEGATORREWARD,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegationDelegatorReward)
  })
_sym_db.RegisterMessage(DelegationDelegatorReward)

CommunityPoolSpendProposalWithDeposit = _reflection.GeneratedProtocolMessageType('CommunityPoolSpendProposalWithDeposit', (_message.Message,), {
  'DESCRIPTOR' : _COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT,
  '__module__' : 'cosmos.distribution.v1beta1.distribution_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.CommunityPoolSpendProposalWithDeposit)
  })
_sym_db.RegisterMessage(CommunityPoolSpendProposalWithDeposit)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['community_tax']._options = None
_PARAMS.fields_by_name['base_proposer_reward']._options = None
_PARAMS.fields_by_name['bonus_proposer_reward']._options = None
_PARAMS.fields_by_name['withdraw_addr_enabled']._options = None
_PARAMS._options = None
_VALIDATORHISTORICALREWARDS.fields_by_name['cumulative_reward_ratio']._options = None
_VALIDATORHISTORICALREWARDS.fields_by_name['reference_count']._options = None
_VALIDATORCURRENTREWARDS.fields_by_name['rewards']._options = None
_VALIDATORACCUMULATEDCOMMISSION.fields_by_name['commission']._options = None
_VALIDATOROUTSTANDINGREWARDS.fields_by_name['rewards']._options = None
_VALIDATORSLASHEVENT.fields_by_name['validator_period']._options = None
_VALIDATORSLASHEVENT.fields_by_name['fraction']._options = None
_VALIDATORSLASHEVENTS.fields_by_name['validator_slash_events']._options = None
_VALIDATORSLASHEVENTS._options = None
_FEEPOOL.fields_by_name['community_pool']._options = None
_COMMUNITYPOOLSPENDPROPOSAL.fields_by_name['amount']._options = None
_COMMUNITYPOOLSPENDPROPOSAL._options = None
_DELEGATORSTARTINGINFO.fields_by_name['previous_period']._options = None
_DELEGATORSTARTINGINFO.fields_by_name['stake']._options = None
_DELEGATORSTARTINGINFO.fields_by_name['height']._options = None
_DELEGATIONDELEGATORREWARD.fields_by_name['validator_address']._options = None
_DELEGATIONDELEGATORREWARD.fields_by_name['reward']._options = None
_DELEGATIONDELEGATORREWARD._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._options = None
_COMMUNITYPOOLSPENDPROPOSALWITHDEPOSIT._options = None
# @@protoc_insertion_point(module_scope)
