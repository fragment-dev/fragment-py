# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PartyListResponse", "Data"]


class Data(BaseModel):
    """Party object"""

    external_id: str = FieldInfo(alias="externalId")
    """External ID for the party"""

    counter_party_type: Optional[str] = FieldInfo(alias="counterPartyType", default=None)
    """Type of the counterparty"""


class PartyListResponse(BaseModel):
    """List of parties"""

    data: List[Data]
