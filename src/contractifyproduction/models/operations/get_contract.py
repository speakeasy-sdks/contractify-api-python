"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contract_read as shared_contract_read
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetContractRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    contract: int = dataclasses.field(metadata={'path_param': { 'field_name': 'contract', 'style': 'simple', 'explode': False }})
    r"""Id of the contract"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetContract404ApplicationJSON:
    r"""Not Found"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetContract403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetContract401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetContract200ApplicationJSON:
    r"""OK"""
    data: Optional[shared_contract_read.ContractRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetContractResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_contract_200_application_json_object: Optional[GetContract200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    get_contract_401_application_json_object: Optional[GetContract401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    get_contract_403_application_json_object: Optional[GetContract403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    get_contract_404_application_json_object: Optional[GetContract404ApplicationJSON] = dataclasses.field(default=None)
    r"""Not Found"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

