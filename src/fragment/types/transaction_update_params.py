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
    """Allocation updates."""

    tags: Tags
    """Tag updates."""


class AllocationsCreateUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class AllocationsCreateUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


AllocationsCreateUser: TypeAlias = Union[AllocationsCreateUserID, AllocationsCreateUserExternalID]


class AllocationsCreate(TypedDict, total=False):
    """An allocation linking a transaction to an invoice."""

    amount: Required[str]
    """
    Allocation amount, as a non-negative string in the smallest currency unit, such
    as cents for USD.
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
    Updated allocation amount, as a non-negative string in the smallest currency
    unit, such as cents for USD.
    """


class Allocations(TypedDict, total=False):
    """Allocation updates."""

    create: Iterable[AllocationsCreate]
    """Allocations to create."""

    update: Iterable[AllocationsUpdate]
    """Allocations to update."""


class TagsCreate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsDelete(TypedDict, total=False):
    key: Required[str]
    """Tag key to delete."""


class TagsSet(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsUpdate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class Tags(TypedDict, total=False):
    """Tag updates."""

    create: Iterable[TagsCreate]
    """Tags to create. The tag key must not already exist."""

    delete: Iterable[TagsDelete]
    """Tags to remove."""

    set: Iterable[TagsSet]
    """Tags to set. Creates a new tag or updates an existing tag."""

    update: Iterable[TagsUpdate]
    """Tags to update. The tag key must already exist."""
