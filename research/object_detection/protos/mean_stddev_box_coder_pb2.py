# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/mean_stddev_box_coder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/mean_stddev_box_coder.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
<<<<<<< Updated upstream
  serialized_pb=_b('\n3object_detection/protos/mean_stddev_box_coder.proto\x12\x17object_detection.protos\"*\n\x12MeanStddevBoxCoder\x12\x14\n\x06stddev\x18\x01 \x01(\x02:\x04\x30.01')
=======
  serialized_pb=_b('\n3object_detection/protos/mean_stddev_box_coder.proto\x12\x17object_detection.protos\"\x14\n\x12MeanStddevBoxCoder')
>>>>>>> Stashed changes
)




_MEANSTDDEVBOXCODER = _descriptor.Descriptor(
  name='MeanStddevBoxCoder',
  full_name='object_detection.protos.MeanStddevBoxCoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
<<<<<<< Updated upstream
    _descriptor.FieldDescriptor(
      name='stddev', full_name='object_detection.protos.MeanStddevBoxCoder.stddev', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
=======
>>>>>>> Stashed changes
  ],
  extensions=[
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
  serialized_start=80,
<<<<<<< Updated upstream
  serialized_end=122,
=======
  serialized_end=100,
>>>>>>> Stashed changes
)

DESCRIPTOR.message_types_by_name['MeanStddevBoxCoder'] = _MEANSTDDEVBOXCODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeanStddevBoxCoder = _reflection.GeneratedProtocolMessageType('MeanStddevBoxCoder', (_message.Message,), dict(
  DESCRIPTOR = _MEANSTDDEVBOXCODER,
  __module__ = 'object_detection.protos.mean_stddev_box_coder_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.MeanStddevBoxCoder)
  ))
_sym_db.RegisterMessage(MeanStddevBoxCoder)


# @@protoc_insertion_point(module_scope)
