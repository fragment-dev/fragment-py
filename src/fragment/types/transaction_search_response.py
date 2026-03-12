# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .transaction import Transaction

__all__ = [
    "TransactionSearchResponse",
    "Data",
    "DataDiff",
    "DataDiffAddAllocationDiffEntry",
    "DataDiffAddAllocationDiffEntryItem",
    "DataDiffAddAllocationDiffEntryItemUser",
    "DataDiffDeleteAllocationDiffEntry",
    "DataDiffDeleteAllocationDiffEntryItem",
    "DataDiffDeleteAllocationDiffEntryItemUser",
]


class DataDiffAddAllocationDiffEntryItemUser(BaseModel):
    id: str
    """FRAGMENT generated ID of the user"""


class DataDiffAddAllocationDiffEntryItem(BaseModel):
    """Transaction allocation against an invoice."""

    amount: str
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice to allocate against."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataDiffAddAllocationDiffEntryItemUser


class DataDiffAddAllocationDiffEntry(BaseModel):
    item: DataDiffAddAllocationDiffEntryItem
    """Transaction allocation against an invoice."""

    op: Literal["add"]
    """An allocation was added"""


class DataDiffDeleteAllocationDiffEntryItemUser(BaseModel):
    id: str
    """FRAGMENT generated ID of the user"""


class DataDiffDeleteAllocationDiffEntryItem(BaseModel):
    """Transaction allocation against an invoice."""

    amount: str
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice to allocate against."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataDiffDeleteAllocationDiffEntryItemUser


class DataDiffDeleteAllocationDiffEntry(BaseModel):
    item: DataDiffDeleteAllocationDiffEntryItem
    """Transaction allocation against an invoice."""

    op: Literal["delete"]
    """An allocation was deleted"""


DataDiff: TypeAlias = Union[DataDiffAddAllocationDiffEntry, DataDiffDeleteAllocationDiffEntry]


class Data(Transaction):
    """A versioned snapshot of a transaction"""

    diff: Optional[List[DataDiff]] = None
    """Allocation changes applied in this version.

    Absent on version 1 (initial creation). Each entry describes an allocation that
    was added or deleted.
    """

    version: Optional[int] = None  # type: ignore
    """Version number of this transaction snapshot."""


class TransactionSearchResponse(BaseModel):
    """Search results for transactions."""

    data: List[Data]
