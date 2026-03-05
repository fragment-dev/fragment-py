# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TransactionCreateAllocationsParams",
    "AllocationUpdate",
    "AllocationUpdateAddAllocationOperation",
    "AllocationUpdateAddAllocationOperationUser",
    "AllocationUpdateAddAllocationOperationUserID",
    "AllocationUpdateAddAllocationOperationUserExternalID",
    "AllocationUpdateDeleteAllocationOperation",
]


class TransactionCreateAllocationsParams(TypedDict, total=False):
    allocation_updates: Required[Iterable[AllocationUpdate]]
    """Allocation operations to apply"""

    version: Required[int]
    """Current transaction version for optimistic concurrency control"""


class AllocationUpdateAddAllocationOperationUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated ID of the user"""


class AllocationUpdateAddAllocationOperationUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user"""


AllocationUpdateAddAllocationOperationUser: TypeAlias = Union[
    AllocationUpdateAddAllocationOperationUserID, AllocationUpdateAddAllocationOperationUserExternalID
]


class AllocationUpdateAddAllocationOperation(TypedDict, total=False):
    amount: Required[str]
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: Required[str]
    """The invoice to allocate against."""

    op: Required[Literal["add"]]
    """Add a new allocation"""

    type: Required[Literal["invoice_payin", "invoice_payout"]]
    """The type of allocation."""

    user: Required[AllocationUpdateAddAllocationOperationUser]


class AllocationUpdateDeleteAllocationOperation(TypedDict, total=False):
    id: Required[str]
    """The ID of the allocation to remove."""

    op: Required[Literal["delete"]]
    """Delete an allocation"""


AllocationUpdate: TypeAlias = Union[AllocationUpdateAddAllocationOperation, AllocationUpdateDeleteAllocationOperation]
