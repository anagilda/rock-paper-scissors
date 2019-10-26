# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='rockpaperscissors',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ngame.proto\x12\x11rockpaperscissors\"6\n\x0bGameRequest\x12\'\n\x04play\x18\x01 \x01(\x0e\x32\x19.rockpaperscissors.Symbol\"\x9b\x01\n\x0cGameResponse\x12-\n\nenemy_play\x18\x01 \x01(\x0e\x32\x19.rockpaperscissors.Symbol\x12\x36\n\x06result\x18\x02 \x01(\x0e\x32&.rockpaperscissors.GameResponse.Result\"$\n\x06Result\x12\x08\n\x04LOSS\x10\x00\x12\x07\n\x03WIN\x10\x01\x12\x07\n\x03TIE\x10\x02*+\n\x06Symbol\x12\x08\n\x04ROCK\x10\x00\x12\t\n\x05PAPER\x10\x01\x12\x0c\n\x08SCISSORS\x10\x02\x32^\n\x11RockPaperScissors\x12I\n\x04Game\x12\x1e.rockpaperscissors.GameRequest\x1a\x1f.rockpaperscissors.GameResponse\"\x00\x62\x06proto3')
)

_SYMBOL = _descriptor.EnumDescriptor(
  name='Symbol',
  full_name='rockpaperscissors.Symbol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROCK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAPER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCISSORS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=247,
  serialized_end=290,
)
_sym_db.RegisterEnumDescriptor(_SYMBOL)

Symbol = enum_type_wrapper.EnumTypeWrapper(_SYMBOL)
ROCK = 0
PAPER = 1
SCISSORS = 2


_GAMERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='rockpaperscissors.GameResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOSS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=209,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_GAMERESPONSE_RESULT)


_GAMEREQUEST = _descriptor.Descriptor(
  name='GameRequest',
  full_name='rockpaperscissors.GameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='play', full_name='rockpaperscissors.GameRequest.play', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=33,
  serialized_end=87,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='GameResponse',
  full_name='rockpaperscissors.GameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enemy_play', full_name='rockpaperscissors.GameResponse.enemy_play', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='rockpaperscissors.GameResponse.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GAMERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=245,
)

_GAMEREQUEST.fields_by_name['play'].enum_type = _SYMBOL
_GAMERESPONSE.fields_by_name['enemy_play'].enum_type = _SYMBOL
_GAMERESPONSE.fields_by_name['result'].enum_type = _GAMERESPONSE_RESULT
_GAMERESPONSE_RESULT.containing_type = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['GameRequest'] = _GAMEREQUEST
DESCRIPTOR.message_types_by_name['GameResponse'] = _GAMERESPONSE
DESCRIPTOR.enum_types_by_name['Symbol'] = _SYMBOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameRequest = _reflection.GeneratedProtocolMessageType('GameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:rockpaperscissors.GameRequest)
  })
_sym_db.RegisterMessage(GameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:rockpaperscissors.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)



_ROCKPAPERSCISSORS = _descriptor.ServiceDescriptor(
  name='RockPaperScissors',
  full_name='rockpaperscissors.RockPaperScissors',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=292,
  serialized_end=386,
  methods=[
  _descriptor.MethodDescriptor(
    name='Game',
    full_name='rockpaperscissors.RockPaperScissors.Game',
    index=0,
    containing_service=None,
    input_type=_GAMEREQUEST,
    output_type=_GAMERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROCKPAPERSCISSORS)

DESCRIPTOR.services_by_name['RockPaperScissors'] = _ROCKPAPERSCISSORS

# @@protoc_insertion_point(module_scope)
