"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import task_collection as shared_task_collection
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class ListTasksRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""The page to retrieve"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListTasks403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListTasks401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class ListTasksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_tasks_401_application_json_object: Optional[ListTasks401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    list_tasks_403_application_json_object: Optional[ListTasks403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    task_collection: Optional[shared_task_collection.TaskCollection] = dataclasses.field(default=None)
    r"""OK"""
    

