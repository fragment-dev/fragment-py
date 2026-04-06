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
    "TagsSet",
    "TagsUpdate",
]


class TransactionUpdateParams(TypedDict, total=False):
    current_transaction_version: Required[int]
    """Current version of the transaction. Must match the stored version."""

    allocations: Allocations

    tags: Tags


class AllocationsCreateUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class AllocationsCreateUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique external ID."""


AllocationsCreateUser: TypeAlias = Union[AllocationsCreateUserID, AllocationsCreateUserExternalID]


class AllocationsCreate(TypedDict, total=False):
    """An allocation linking a transaction to an invoice."""

    amount: Required[str]
    """
    Allocation amount, as a positive string in the smallest unit of the currency
    (for example, cents for USD).
    """

    invoice_id: Required[str]
    """Invoice to allocate against."""

    type: Required[Literal["invoice_payin", "invoice_payout"]]
    """Type of allocation."""

    user: Required[AllocationsCreateUser]
    """Identifies a user by `id` or `external_id`."""


class AllocationsUpdate(TypedDict, total=False):
    id: Required[str]
    """Allocation to update."""

    amount: Required[str]
    """
    Updated allocation amount, as a positive string in the smallest unit of the
    currency (for example, cents for USD).
    """


class Allocations(TypedDict, total=False):
    create: Iterable[AllocationsCreate]
    """Creates a new allocation."""

    update: Iterable[AllocationsUpdate]
    """Updates an existing allocation."""


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


class TagsSet(TypedDict, total=False):
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
    """Tags to add. Prefer `set` unless you specifically want create-only validation."""

    delete: Iterable[TagsDelete]
    """Tags to remove by key."""

    set: Iterable[TagsSet]
    """
    Tags to create or overwrite without requiring the caller to distinguish between
    create and update.
    """

    update: Iterable[TagsUpdate]
    """Tags to update.

    The key identifies the existing tag; the value is the new value. Prefer `set`
    unless you specifically want update-only validation.
    """
