# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionSearchAllocationsResponse", "Data", "DataTransaction", "DataUser"]


class DataTransaction(BaseModel):
    """Transaction the allocation is applied to."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class DataUser(BaseModel):
    """User associated with the allocation."""

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
    Allocated amount, as a non-negative string in the smallest currency unit, such
    as cents for USD.
    """

    invoice_id: str
    """Invoice the allocation is applied against."""

    posted: datetime
    """Timestamp when the parent transaction was posted. Uses ISO 8601 format."""

    transaction: DataTransaction
    """Transaction the allocation is applied to."""

    type: Literal["invoice_payin", "invoice_payout"]
    """Type of allocation."""

    user: DataUser
    """User associated with the allocation."""


class TransactionSearchAllocationsResponse(BaseModel):
    data: List[Data]
    """List of allocation search results."""
