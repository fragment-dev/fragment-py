# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TransactionUpdateParams",
    "Allocations",
    "AllocationsCreate",
    "AllocationsCreateUser",
    "AllocationsCreateUserID",
    "AllocationsCreateUserExternalID",
    "AllocationsUpdate",
    "Tags",
    "TagsCreate",
    "TagsDelete",
    "TagsUpdate",
]


class TransactionUpdateParams(TypedDict, total=False):
    current_transaction_version: Required[int]
    """Current transaction version for optimistic concurrency control."""

    allocations: Allocations

    tags: Tags


class AllocationsCreateUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated ID of the user"""


class AllocationsCreateUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user"""


AllocationsCreateUser: TypeAlias = Union[AllocationsCreateUserID, AllocationsCreateUserExternalID]


class AllocationsCreate(TypedDict, total=False):
    """Transaction allocation against an invoice."""

    amount: Required[str]
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: Required[str]
    """The invoice to allocate against."""

    type: Required[Literal["invoice_payin", "invoice_payout"]]
    """The type of allocation."""

    user: Required[AllocationsCreateUser]
    """Identifies a user by Fragment-generated id or external_id (request body)."""


class AllocationsUpdate(TypedDict, total=False):
    id: Required[str]
    """The ID of the allocation to update."""

    amount: Required[str]
    """New amount in smallest currency unit as stringified bigint."""


class Allocations(TypedDict, total=False):
    create: Iterable[AllocationsCreate]
    """Allocations to add to the transaction"""

    update: Iterable[AllocationsUpdate]
    """Existing allocations to update"""


class TagsCreate(TypedDict, total=False):
    """A key-value tag pair for metadata"""

    key: Required[str]
    """Tag key.

    Must be a valid safe string (no special characters like #, /, :). Max 50
    characters.
    """

    value: Required[str]
    """Tag value.

    Must be a valid safe string (no special characters like #, /, :). Max 200
    characters.
    """


class TagsDelete(TypedDict, total=False):
    key: Required[str]
    """Tag key to delete"""


class TagsUpdate(TypedDict, total=False):
    """A key-value tag pair for metadata"""

    key: Required[str]
    """Tag key.

    Must be a valid safe string (no special characters like #, /, :). Max 50
    characters.
    """

    value: Required[str]
    """Tag value.

    Must be a valid safe string (no special characters like #, /, :). Max 200
    characters.
    """


class Tags(TypedDict, total=False):
    create: Iterable[TagsCreate]
    """Tags to add"""

    delete: Iterable[TagsDelete]
    """Tags to remove by key"""

    update: Iterable[TagsUpdate]
    """Tags to update.

    The key identifies the existing tag; the value is the new value.
    """
