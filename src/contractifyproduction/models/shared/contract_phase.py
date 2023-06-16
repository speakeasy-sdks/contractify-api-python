"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ContractPhase(str, Enum):
    TENDER = 'tender'
    ONGOING = 'ongoing'
    IN_TERMINATION = 'in_termination'
    ENDED = 'ended'
    IN_REVIEW = 'in_review'