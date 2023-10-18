"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import department_read as shared_department_read
from ..shared import department_write as shared_department_write
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclasses.dataclass
class UpdateDepartmentRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    department: int = dataclasses.field(metadata={'path_param': { 'field_name': 'department', 'style': 'simple', 'explode': False }})
    r"""Id of the department"""
    department_write: Optional[shared_department_write.DepartmentWrite] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment422ApplicationJSONErrors:
    errors: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment422ApplicationJSON:
    r"""Invalid data posted"""
    errors: Optional[List[UpdateDepartment422ApplicationJSONErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartment200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_department_read.DepartmentRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class UpdateDepartmentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_department_200_application_json_object: Optional[UpdateDepartment200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    update_department_401_application_json_object: Optional[UpdateDepartment401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    update_department_403_application_json_object: Optional[UpdateDepartment403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    update_department_404_application_json_object: Optional[UpdateDepartment404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    update_department_422_application_json_object: Optional[UpdateDepartment422ApplicationJSON] = dataclasses.field(default=None)
    r"""Invalid data posted"""
    

