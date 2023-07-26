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
class CreateRelationSecurity:
    o_auth2: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    personal_access_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class CreateRelationRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    relation_write: Optional[shared_relation_write.RelationWrite] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRelation422ApplicationJSONErrors:
    errors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRelation422ApplicationJSON:
    r"""Invalid data posted"""
    errors: Optional[list[CreateRelation422ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRelation403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRelation401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateRelation201ApplicationJSON:
    r"""Created"""
    data: Optional[shared_relation_read.RelationRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class CreateRelationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_relation_201_application_json_object: Optional[CreateRelation201ApplicationJSON] = dataclasses.field(default=None)
    r"""Created"""
    create_relation_401_application_json_object: Optional[CreateRelation401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    create_relation_403_application_json_object: Optional[CreateRelation403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    create_relation_422_application_json_object: Optional[CreateRelation422ApplicationJSON] = dataclasses.field(default=None)
    r"""Invalid data posted"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

