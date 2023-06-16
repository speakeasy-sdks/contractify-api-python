"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import contract_automaticrenewal as shared_contract_automaticrenewal
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContractRenewal:
    automatic_renewal: Optional[shared_contract_automaticrenewal.ContractAutomaticRenewal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automatic_renewal'), 'exclude': lambda f: f is None }})
    is_automatically_renewed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_automatically_renewed'), 'exclude': lambda f: f is None }})
    
