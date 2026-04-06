# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionSearchAllocationsResponse", "Data", "DataTransaction", "DataUser"]


class DataTransaction(BaseModel):
    """Transaction reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class DataUser(BaseModel):
    """User reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class Data(BaseModel):
    """An allocation with a reference to its parent transaction."""

    id: str
    """FRAGMENT generated unique ID."""

    amount: str
    """
    Allocated amount, as a positive string in the smallest unit of the currency (for
    example, cents for USD).
    """

    invoice_id: str
    """Invoice the allocation is applied against."""

    posted: datetime
    """Timestamp when the parent transaction was posted. Uses ISO 8601 format."""

    transaction: DataTransaction
    """Transaction reference."""

    type: Literal["invoice_payin", "invoice_payout"]
    """Type of allocation."""

    user: DataUser
    """User reference."""


class TransactionSearchAllocationsResponse(BaseModel):
    data: List[Data]
    """List of allocation search results."""
