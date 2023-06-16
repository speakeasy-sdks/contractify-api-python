"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import document_read as shared_document_read
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class GetDocumentSecurity:
    o_auth2: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    personal_access_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetDocumentRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    document: int = dataclasses.field(metadata={'path_param': { 'field_name': 'document', 'style': 'simple', 'explode': False }})
    r"""Id of the document"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetDocument404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetDocument403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetDocument401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetDocument200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_document_read.DocumentRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetDocumentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_document_200_application_json_object: Optional[GetDocument200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    get_document_401_application_json_object: Optional[GetDocument401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    get_document_403_application_json_object: Optional[GetDocument403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    get_document_404_application_json_object: Optional[GetDocument404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
