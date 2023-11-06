"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class DeleteTaskRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    task: int = dataclasses.field(metadata={'path_param': { 'field_name': 'task', 'style': 'simple', 'explode': False }})
    r"""Id of the task"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteTask404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteTask403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteTask401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class DeleteTaskResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_task_401_application_json_object: Optional[DeleteTask401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    delete_task_403_application_json_object: Optional[DeleteTask403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    delete_task_404_application_json_object: Optional[DeleteTask404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

