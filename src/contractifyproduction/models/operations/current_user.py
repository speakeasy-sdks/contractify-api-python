"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user_current as shared_user_current
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CurrentUser403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CurrentUser401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CurrentUser200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_user_current.UserCurrent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class CurrentUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    current_user_200_application_json_object: Optional[CurrentUser200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    current_user_401_application_json_object: Optional[CurrentUser401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    current_user_403_application_json_object: Optional[CurrentUser403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

