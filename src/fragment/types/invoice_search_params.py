# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvoiceSearchParams", "Filter", "FilterTags", "FilterTagsAll", "FilterTagsAny", "PageInfo"]


class InvoiceSearchParams(TypedDict, total=False):
    filter: Required[Filter]
    """Filter criteria for the search."""

    page_info: Required[PageInfo]
    """Pagination parameters."""


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
    """Returns invoices matching every specified tag (AND)."""

    any: Iterable[FilterTagsAny]
    """Returns invoices matching at least one of the specified tags (OR)."""


class Filter(TypedDict, total=False):
    """Filter criteria for the search."""

    status: Literal["open"]
    """Filter by invoice status.

    `open` returns invoices with non-zero clearing account balances.
    """

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
