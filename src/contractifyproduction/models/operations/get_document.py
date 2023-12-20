"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import document_read as shared_document_read
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetDocumentRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    document: int = dataclasses.field(metadata={'path_param': { 'field_name': 'document', 'style': 'simple', 'explode': False }})
    r"""Id of the document"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDocumentResponseBody:
    r"""OK"""
    data: Optional[shared_document_read.DocumentRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetDocumentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[GetDocumentResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

