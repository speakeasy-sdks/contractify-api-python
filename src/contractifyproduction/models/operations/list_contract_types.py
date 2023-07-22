"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contracttype_collection as shared_contracttype_collection
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class ListContractTypesSecurity:
    o_auth2: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    personal_access_token: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class ListContractTypesRequest:
    company: int = dataclasses.field(metadata={'path_param': { 'field_name': 'company', 'style': 'simple', 'explode': False }})
    r"""Id of the company"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListContractTypes403ApplicationJSON:
    r"""Forbidden"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListContractTypes401ApplicationJSON:
    r"""Unauthenticated"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class ListContractTypesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    contract_type_collection: Optional[shared_contracttype_collection.ContractTypeCollection] = dataclasses.field(default=None)
    r"""OK"""
    list_contract_types_401_application_json_object: Optional[ListContractTypes401ApplicationJSON] = dataclasses.field(default=None)
    r"""Unauthenticated"""
    list_contract_types_403_application_json_object: Optional[ListContractTypes403ApplicationJSON] = dataclasses.field(default=None)
    r"""Forbidden"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

