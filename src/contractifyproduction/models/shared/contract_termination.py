"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from contractifyproduction import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContractTermination:
    is_terminable_at_any_time: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_terminable_at_any_time'), 'exclude': lambda f: f is None }})
    termination_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termination_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat }})
    termination_duration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termination_duration') }})
    

