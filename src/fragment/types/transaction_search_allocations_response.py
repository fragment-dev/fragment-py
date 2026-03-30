# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionSearchAllocationsResponse", "Data", "DataTransaction", "DataUser"]


class DataTransaction(BaseModel):
    """Reference to a transaction by encoded ID and external ID."""

    id: str
    """Encoded transaction ID."""

    external_id: str
    """External transaction ID."""


class DataUser(BaseModel):
    """User reference in API responses: Fragment user id and external_id."""

    id: str
    """FRAGMENT generated ID of the user"""

    external_id: str
    """External ID of the user"""


class Data(BaseModel):
    """A flattened allocation with a reference to its parent transaction."""

    id: str
    """Allocation ID."""

    amount: str
    """Allocated amount in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice this allocation is applied against."""

    posted: datetime
    """Posted timestamp of the parent transaction in ISO 8601 format."""

    transaction: DataTransaction
    """Reference to a transaction by encoded ID and external ID."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataUser
    """User reference in API responses: Fragment user id and external_id."""


class TransactionSearchAllocationsResponse(BaseModel):
    """Search results for transaction allocations."""

    data: List[Data]
