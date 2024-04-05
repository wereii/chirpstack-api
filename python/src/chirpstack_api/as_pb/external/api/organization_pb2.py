# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/organization.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4chirpstack-api/as_pb/external/api/organization.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x8e\x01\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x19\n\x11\x63\x61n_have_gateways\x18\x04 \x01(\x08\x12\x19\n\x11max_gateway_count\x18\x05 \x01(\r\x12\x18\n\x10max_device_count\x18\x06 \x01(\r\"\xc1\x01\n\x14OrganizationListItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x19\n\x11\x63\x61n_have_gateways\x18\x04 \x01(\x08\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"$\n\x16GetOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\xa2\x01\n\x17GetOrganizationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"D\n\x19\x43reateOrganizationRequest\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"(\n\x1a\x43reateOrganizationResponse\x12\n\n\x02id\x18\x01 \x01(\x03\"D\n\x19UpdateOrganizationRequest\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"\'\n\x19\x44\x65leteOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"H\n\x17ListOrganizationRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06search\x18\x03 \x01(\t\"Z\n\x18ListOrganizationResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12)\n\x06result\x18\x02 \x03(\x0b\x32\x19.api.OrganizationListItem\"\xa8\x01\n\x10OrganizationUser\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x17\n\x07user_id\x18\x02 \x01(\x03R\x06userID\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x05 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x06 \x01(\x08\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"\xe7\x01\n\x18OrganizationUserListItem\x12\x17\n\x07user_id\x18\x01 \x01(\x03R\x06userID\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x06 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x07 \x01(\x08\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"N\n\x1a\x41\x64\x64OrganizationUserRequest\x12\x30\n\x11organization_user\x18\x01 \x01(\x0b\x32\x15.api.OrganizationUser\"Q\n\x1dUpdateOrganizationUserRequest\x12\x30\n\x11organization_user\x18\x01 \x01(\x0b\x32\x15.api.OrganizationUser\"a\n\x1d\x44\x65leteOrganizationUserRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x17\n\x07user_id\x18\x02 \x01(\x03R\x06userID\"f\n\x1cListOrganizationUsersRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"c\n\x1dListOrganizationUsersResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12-\n\x06result\x18\x02 \x03(\x0b\x32\x1d.api.OrganizationUserListItem\"^\n\x1aGetOrganizationUserRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x17\n\x07user_id\x18\x02 \x01(\x03R\x06userID\"\xaf\x01\n\x1bGetOrganizationUserResponse\x12\x30\n\x11organization_user\x18\x01 \x01(\x0b\x32\x15.api.OrganizationUser\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xf6\t\n\x13OrganizationService\x12_\n\x04List\x12\x1c.api.ListOrganizationRequest\x1a\x1d.api.ListOrganizationResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/organizations\x12\x61\n\x03Get\x12\x1b.api.GetOrganizationRequest\x1a\x1c.api.GetOrganizationResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/api/organizations/{id}\x12h\n\x06\x43reate\x12\x1e.api.CreateOrganizationRequest\x1a\x1f.api.CreateOrganizationResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/api/organizations:\x01*\x12q\n\x06Update\x12\x1e.api.UpdateOrganizationRequest\x1a\x16.google.protobuf.Empty\"/\x82\xd3\xe4\x93\x02)\x1a$/api/organizations/{organization.id}:\x01*\x12\x61\n\x06\x44\x65lete\x12\x1e.api.DeleteOrganizationRequest\x1a\x16.google.protobuf.Empty\"\x1f\x82\xd3\xe4\x93\x02\x19*\x17/api/organizations/{id}\x12\x86\x01\n\tListUsers\x12!.api.ListOrganizationUsersRequest\x1a\".api.ListOrganizationUsersResponse\"2\x82\xd3\xe4\x93\x02,\x12*/api/organizations/{organization_id}/users\x12\x8a\x01\n\x07GetUser\x12\x1f.api.GetOrganizationUserRequest\x1a .api.GetOrganizationUserResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/api/organizations/{organization_id}/users/{user_id}\x12\x8b\x01\n\x07\x41\x64\x64User\x12\x1f.api.AddOrganizationUserRequest\x1a\x16.google.protobuf.Empty\"G\x82\xd3\xe4\x93\x02\x41\"</api/organizations/{organization_user.organization_id}/users:\x01*\x12\xad\x01\n\nUpdateUser\x12\".api.UpdateOrganizationUserRequest\x1a\x16.google.protobuf.Empty\"c\x82\xd3\xe4\x93\x02]\x1aX/api/organizations/{organization_user.organization_id}/users/{organization_user.user_id}:\x01*\x12\x86\x01\n\nDeleteUser\x12\".api.DeleteOrganizationUserRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02\x36*4/api/organizations/{organization_id}/users/{user_id}Bp\n!io.chirpstack.api.as.external.apiB\x11OrganizationProtoP\x01Z6github.com/wereii/chirpstack-api/go/v3/as/external/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.organization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\021OrganizationProtoP\001Z6github.com/wereii/chirpstack-api/go/v3/as/external/api'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['List']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\024\022\022/api/organizations'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Get']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\031\022\027/api/organizations/{id}'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Create']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\027\"\022/api/organizations:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Update']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002)\032$/api/organizations/{organization.id}:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Delete']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\031*\027/api/organizations/{id}'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListUsers']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['ListUsers']._serialized_options = b'\202\323\344\223\002,\022*/api/organizations/{organization_id}/users'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['GetUser']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['GetUser']._serialized_options = b'\202\323\344\223\0026\0224/api/organizations/{organization_id}/users/{user_id}'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['AddUser']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['AddUser']._serialized_options = b'\202\323\344\223\002A\"</api/organizations/{organization_user.organization_id}/users:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['UpdateUser']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['UpdateUser']._serialized_options = b'\202\323\344\223\002]\032X/api/organizations/{organization_user.organization_id}/users/{organization_user.user_id}:\001*'
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['DeleteUser']._options = None
  _globals['_ORGANIZATIONSERVICE'].methods_by_name['DeleteUser']._serialized_options = b'\202\323\344\223\0026*4/api/organizations/{organization_id}/users/{user_id}'
  _globals['_ORGANIZATION']._serialized_start=154
  _globals['_ORGANIZATION']._serialized_end=296
  _globals['_ORGANIZATIONLISTITEM']._serialized_start=299
  _globals['_ORGANIZATIONLISTITEM']._serialized_end=492
  _globals['_GETORGANIZATIONREQUEST']._serialized_start=494
  _globals['_GETORGANIZATIONREQUEST']._serialized_end=530
  _globals['_GETORGANIZATIONRESPONSE']._serialized_start=533
  _globals['_GETORGANIZATIONRESPONSE']._serialized_end=695
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_start=697
  _globals['_CREATEORGANIZATIONREQUEST']._serialized_end=765
  _globals['_CREATEORGANIZATIONRESPONSE']._serialized_start=767
  _globals['_CREATEORGANIZATIONRESPONSE']._serialized_end=807
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_start=809
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_end=877
  _globals['_DELETEORGANIZATIONREQUEST']._serialized_start=879
  _globals['_DELETEORGANIZATIONREQUEST']._serialized_end=918
  _globals['_LISTORGANIZATIONREQUEST']._serialized_start=920
  _globals['_LISTORGANIZATIONREQUEST']._serialized_end=992
  _globals['_LISTORGANIZATIONRESPONSE']._serialized_start=994
  _globals['_LISTORGANIZATIONRESPONSE']._serialized_end=1084
  _globals['_ORGANIZATIONUSER']._serialized_start=1087
  _globals['_ORGANIZATIONUSER']._serialized_end=1255
  _globals['_ORGANIZATIONUSERLISTITEM']._serialized_start=1258
  _globals['_ORGANIZATIONUSERLISTITEM']._serialized_end=1489
  _globals['_ADDORGANIZATIONUSERREQUEST']._serialized_start=1491
  _globals['_ADDORGANIZATIONUSERREQUEST']._serialized_end=1569
  _globals['_UPDATEORGANIZATIONUSERREQUEST']._serialized_start=1571
  _globals['_UPDATEORGANIZATIONUSERREQUEST']._serialized_end=1652
  _globals['_DELETEORGANIZATIONUSERREQUEST']._serialized_start=1654
  _globals['_DELETEORGANIZATIONUSERREQUEST']._serialized_end=1751
  _globals['_LISTORGANIZATIONUSERSREQUEST']._serialized_start=1753
  _globals['_LISTORGANIZATIONUSERSREQUEST']._serialized_end=1855
  _globals['_LISTORGANIZATIONUSERSRESPONSE']._serialized_start=1857
  _globals['_LISTORGANIZATIONUSERSRESPONSE']._serialized_end=1956
  _globals['_GETORGANIZATIONUSERREQUEST']._serialized_start=1958
  _globals['_GETORGANIZATIONUSERREQUEST']._serialized_end=2052
  _globals['_GETORGANIZATIONUSERRESPONSE']._serialized_start=2055
  _globals['_GETORGANIZATIONUSERRESPONSE']._serialized_end=2230
  _globals['_ORGANIZATIONSERVICE']._serialized_start=2233
  _globals['_ORGANIZATIONSERVICE']._serialized_end=3503
# @@protoc_insertion_point(module_scope)
