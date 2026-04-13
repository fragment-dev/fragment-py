# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "TransactionSearchParams",
    "Filter",
    "FilterAccount",
    "FilterAccountAny",
    "FilterTags",
    "FilterTagsAll",
    "FilterTagsAny",
    "PageInfo",
]


class TransactionSearchParams(TypedDict, total=False):
    filter: Required[Filter]
    """Filter for searching transactions."""

    page_info: PageInfo
    """Pagination parameters."""


class FilterAccountAny(TypedDict, total=False):
    """External account for the transaction.

    Identify it by `id`, `external_id`, or both.
    """

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class FilterAccount(TypedDict, total=False):
    """Account filter."""

    any: Required[Iterable[FilterAccountAny]]
    """Match transactions belonging to any of these accounts, using OR logic."""


class FilterTagsAll(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterTagsAny(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterTags(TypedDict, total=False):
    """Tag-based filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all` AND at least one entry in `any`.
    """

    all: Iterable[FilterTagsAll]
    """Returns transactions matching every specified tag, using AND logic."""

    any: Iterable[FilterTagsAny]
    """
    Returns transactions matching at least one of the specified tags, using OR
    logic.
    """


class Filter(TypedDict, total=False):
    """Filter for searching transactions."""

    account: FilterAccount
    """Account filter."""

    tags: FilterTags
    """Tag-based filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all`
    AND at least one entry in `any`.
    """


class PageInfo(TypedDict, total=False):
    """Pagination parameters."""

    after: str
    """Cursor for fetching the next page of results."""

    limit: int
    """Number of results to return. Defaults to 20."""
