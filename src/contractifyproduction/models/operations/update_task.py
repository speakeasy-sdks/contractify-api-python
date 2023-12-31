"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import task_read as shared_task_read
from ...models.shared import task_update as shared_task_update
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class UpdateTaskRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    task: int = dataclasses.field(metadata={'path_param': { 'field_name': 'task', 'style': 'simple', 'explode': False }})
    r"""Id of the task"""
    task_update: Optional[shared_task_update.TaskUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateTaskResponseBody:
    r"""OK"""
    data: Optional[shared_task_read.TaskRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class UpdateTaskResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[UpdateTaskResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

