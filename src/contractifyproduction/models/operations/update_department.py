"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import department_read as shared_department_read
from ...models.shared import department_write as shared_department_write
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class UpdateDepartmentRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    department: int = dataclasses.field(metadata={'path_param': { 'field_name': 'department', 'style': 'simple', 'explode': False }})
    r"""Id of the department"""
    department_write: Optional[shared_department_write.DepartmentWrite] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateDepartmentResponseBody:
    r"""OK"""
    data: Optional[shared_department_read.DepartmentRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class UpdateDepartmentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    two_hundred_application_json_object: Optional[UpdateDepartmentResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

