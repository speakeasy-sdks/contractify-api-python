"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import department_collection as shared_department_collection
from typing import Optional


@dataclasses.dataclass
class ListDepartmentsRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    



@dataclasses.dataclass
class ListDepartmentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    department_collection: Optional[shared_department_collection.DepartmentCollection] = dataclasses.field(default=None)
    r"""OK"""
    

