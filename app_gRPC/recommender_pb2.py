# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommender.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recommender.proto',
  package='recommender.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11recommender.proto\x12\x0erecommender.v1\"\"\n\x10RecommendRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"*\n\x11RecommendResponse\x12\x15\n\rrestaurantIds\x18\x01 \x03(\t2a\n\x0bRecommender\x12R\n\tRecommend\x12 .recommender.v1.RecommendRequest\x1a!.recommender.v1.RecommendResponse\"\x00\x62\x06proto3'
)




_RECOMMENDREQUEST = _descriptor.Descriptor(
  name='RecommendRequest',
  full_name='recommender.v1.RecommendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='recommender.v1.RecommendRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=37,
  serialized_end=71,
)


_RECOMMENDRESPONSE = _descriptor.Descriptor(
  name='RecommendResponse',
  full_name='recommender.v1.RecommendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='restaurantIds', full_name='recommender.v1.RecommendResponse.restaurantIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['RecommendRequest'] = _RECOMMENDREQUEST
DESCRIPTOR.message_types_by_name['RecommendResponse'] = _RECOMMENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendRequest = _reflection.GeneratedProtocolMessageType('RecommendRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDREQUEST,
  '__module__' : 'recommender_pb2'
  # @@protoc_insertion_point(class_scope:recommender.v1.RecommendRequest)
  })
_sym_db.RegisterMessage(RecommendRequest)

RecommendResponse = _reflection.GeneratedProtocolMessageType('RecommendResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDRESPONSE,
  '__module__' : 'recommender_pb2'
  # @@protoc_insertion_point(class_scope:recommender.v1.RecommendResponse)
  })
_sym_db.RegisterMessage(RecommendResponse)



_RECOMMENDER = _descriptor.ServiceDescriptor(
  name='Recommender',
  full_name='recommender.v1.Recommender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=117,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recommend',
    full_name='recommender.v1.Recommender.Recommend',
    index=0,
    containing_service=None,
    input_type=_RECOMMENDREQUEST,
    output_type=_RECOMMENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDER)

DESCRIPTOR.services_by_name['Recommender'] = _RECOMMENDER

# @@protoc_insertion_point(module_scope)
