# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: archive_restore.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'archive_restore.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61rchive_restore.proto\x12\x0f\x66unctionservice\"9\n\x0f\x46unctionRequest\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"4\n\x10\x46unctionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd5\x01\n\x15\x41rchiveRestoreService\x12]\n\x16\x41rchiveFunctionVersion\x12 .functionservice.FunctionRequest\x1a!.functionservice.FunctionResponse\x12]\n\x16RestoreArchivedVersion\x12 .functionservice.FunctionRequest\x1a!.functionservice.FunctionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'archive_restore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FUNCTIONREQUEST']._serialized_start=42
  _globals['_FUNCTIONREQUEST']._serialized_end=99
  _globals['_FUNCTIONRESPONSE']._serialized_start=101
  _globals['_FUNCTIONRESPONSE']._serialized_end=153
  _globals['_ARCHIVERESTORESERVICE']._serialized_start=156
  _globals['_ARCHIVERESTORESERVICE']._serialized_end=369
# @@protoc_insertion_point(module_scope)