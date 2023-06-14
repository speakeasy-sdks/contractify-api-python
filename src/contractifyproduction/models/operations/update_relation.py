"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import relation_read as shared_relation_read
from ..shared import relation_write as shared_relation_write
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class UpdateRelationSecurity:
    o_auth2: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    personal_access_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class UpdateRelationRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    relation: int = dataclasses.field(metadata={'path_param': { 'field_name': 'relation', 'style': 'simple', 'explode': False }})
    r"""Id of the relation"""
    relation_write: Optional[shared_relation_write.RelationWrite] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation422ApplicationJSONErrors:
    errors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation422ApplicationJSON:
    r"""Invalid data posted"""
    errors: Optional[list[UpdateRelation422ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateRelation200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_relation_read.RelationRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UpdateRelationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_relation_200_application_json_object: Optional[UpdateRelation200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    update_relation_401_application_json_object: Optional[UpdateRelation401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    update_relation_403_application_json_object: Optional[UpdateRelation403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    update_relation_404_application_json_object: Optional[UpdateRelation404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    update_relation_422_application_json_object: Optional[UpdateRelation422ApplicationJSON] = dataclasses.field(default=None)
    r"""Invalid data posted"""
    

