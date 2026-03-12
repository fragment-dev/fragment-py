# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionSearchAllocationsResponse", "Data", "DataTransaction", "DataUser"]


class DataTransaction(BaseModel):
    """Reference to the parent transaction."""

    id: str
    """Encoded transaction ID."""

    external_id: str
    """External transaction ID."""


class DataUser(BaseModel):
    id: str
    """FRAGMENT generated ID of the user"""

    external_id: Optional[str] = None
    """External ID of the user"""


class Data(BaseModel):
    """A flattened allocation with a reference to its parent transaction."""

    id: str
    """Allocation ID."""

    amount: str
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice to allocate against."""

    transaction: DataTransaction
    """Reference to the parent transaction."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataUser


class TransactionSearchAllocationsResponse(BaseModel):
    """Search results for transaction allocations."""

    data: List[Data]
