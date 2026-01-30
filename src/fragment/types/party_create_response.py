# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PartyCreateResponse", "Data"]


class Data(BaseModel):
    """Party object"""

    external_id: str = FieldInfo(alias="externalId")
    """External ID for the party"""

    counter_party_type: Optional[str] = FieldInfo(alias="counterPartyType", default=None)
    """Type of the counterparty"""


class PartyCreateResponse(BaseModel):
    data: Data
    """Party object"""
