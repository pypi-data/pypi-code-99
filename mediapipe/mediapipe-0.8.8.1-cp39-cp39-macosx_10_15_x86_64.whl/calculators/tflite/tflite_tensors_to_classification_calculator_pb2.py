# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tflite/tflite_tensors_to_classification_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/tflite/tflite_tensors_to_classification_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nNmediapipe/calculators/tflite/tflite_tensors_to_classification_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xfc\x01\n.TfLiteTensorsToClassificationCalculatorOptions\x12\x1b\n\x13min_score_threshold\x18\x01 \x01(\x02\x12\r\n\x05top_k\x18\x02 \x01(\x05\x12\x16\n\x0elabel_map_path\x18\x03 \x01(\t\x12\x1d\n\x15\x62inary_classification\x18\x04 \x01(\x08\x32g\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe7\xdd\x83\x7f \x01(\x0b\x32\x39.mediapipe.TfLiteTensorsToClassificationCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TfLiteTensorsToClassificationCalculatorOptions',
  full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_score_threshold', full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions.min_score_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_k', full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions.top_k', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions.label_map_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='binary_classification', full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions.binary_classification', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TfLiteTensorsToClassificationCalculatorOptions.ext', index=0,
      number=266399463, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=132,
  serialized_end=384,
)

DESCRIPTOR.message_types_by_name['TfLiteTensorsToClassificationCalculatorOptions'] = _TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TfLiteTensorsToClassificationCalculatorOptions = _reflection.GeneratedProtocolMessageType('TfLiteTensorsToClassificationCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tflite.tflite_tensors_to_classification_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TfLiteTensorsToClassificationCalculatorOptions)
  })
_sym_db.RegisterMessage(TfLiteTensorsToClassificationCalculatorOptions)

_TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TFLITETENSORSTOCLASSIFICATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
