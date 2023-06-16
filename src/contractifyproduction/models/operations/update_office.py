"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import office_read as shared_office_read
from ..shared import office_write as shared_office_write
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class UpdateOfficeSecurity:
    o_auth2: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    personal_access_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class UpdateOfficeRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    office: int = dataclasses.field(metadata={'path_param': { 'field_name': 'office', 'style': 'simple', 'explode': False }})
    r"""Id of the office"""
    office_write: Optional[shared_office_write.OfficeWrite] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice422ApplicationJSONErrors:
    errors: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice422ApplicationJSON:
    r"""Invalid data posted"""
    errors: Optional[list[UpdateOffice422ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateOffice200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_office_read.OfficeRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UpdateOfficeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_office_200_application_json_object: Optional[UpdateOffice200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    update_office_401_application_json_object: Optional[UpdateOffice401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    update_office_403_application_json_object: Optional[UpdateOffice403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    update_office_404_application_json_object: Optional[UpdateOffice404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    update_office_422_application_json_object: Optional[UpdateOffice422ApplicationJSON] = dataclasses.field(default=None)
    r"""Invalid data posted"""
    
