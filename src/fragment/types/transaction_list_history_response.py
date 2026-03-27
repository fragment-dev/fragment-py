# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .transaction import Transaction

__all__ = [
    "TransactionListHistoryResponse",
    "Data",
    "DataDiff",
    "DataDiffAddAllocationDiffEntry",
    "DataDiffAddAllocationDiffEntryItem",
    "DataDiffAddAllocationDiffEntryItemUser",
    "DataDiffDeleteAllocationDiffEntry",
    "DataDiffDeleteAllocationDiffEntryItem",
    "DataDiffDeleteAllocationDiffEntryItemUser",
    "DataDiffUpdateAllocationDiffEntry",
]


class DataDiffAddAllocationDiffEntryItemUser(BaseModel):
    """User reference in API responses: Fragment user id and optional external_id."""

    id: str
    """FRAGMENT generated ID of the user"""

    external_id: Optional[str] = None
    """External ID of the user"""


class DataDiffAddAllocationDiffEntryItem(BaseModel):
    """Transaction allocation against an invoice."""

    amount: str
    """Allocated amount in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice this allocation is applied against."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataDiffAddAllocationDiffEntryItemUser
    """User reference in API responses: Fragment user id and optional external_id."""


class DataDiffAddAllocationDiffEntry(BaseModel):
    item: DataDiffAddAllocationDiffEntryItem
    """Transaction allocation against an invoice."""

    op: Literal["add"]
    """An allocation was added"""


class DataDiffDeleteAllocationDiffEntryItemUser(BaseModel):
    """User reference in API responses: Fragment user id and optional external_id."""

    id: str
    """FRAGMENT generated ID of the user"""

    external_id: Optional[str] = None
    """External ID of the user"""


class DataDiffDeleteAllocationDiffEntryItem(BaseModel):
    """Transaction allocation against an invoice."""

    amount: str
    """Allocated amount in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice this allocation is applied against."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: DataDiffDeleteAllocationDiffEntryItemUser
    """User reference in API responses: Fragment user id and optional external_id."""


class DataDiffDeleteAllocationDiffEntry(BaseModel):
    item: DataDiffDeleteAllocationDiffEntryItem
    """Transaction allocation against an invoice."""

    op: Literal["delete"]
    """An allocation was deleted"""


class DataDiffUpdateAllocationDiffEntry(BaseModel):
    id: str
    """The ID of the updated allocation."""

    new_amount: str
    """New amount in smallest currency unit as stringified bigint."""

    old_amount: str
    """Previous amount in smallest currency unit as stringified bigint."""

    op: Literal["update"]
    """An allocation was updated"""


DataDiff: TypeAlias = Union[
    DataDiffAddAllocationDiffEntry, DataDiffDeleteAllocationDiffEntry, DataDiffUpdateAllocationDiffEntry
]


class Data(Transaction):
    """A versioned snapshot of a transaction"""

    diff: Optional[List[DataDiff]] = None
    """Allocation changes applied in this version.

    Absent on version 1 (initial creation). Each entry describes an allocation that
    was added or deleted.
    """

    version: Optional[int] = None  # type: ignore
    """Version number of this transaction snapshot."""


class TransactionListHistoryResponse(BaseModel):
    """Version history of a transaction"""

    data: List[Data]
