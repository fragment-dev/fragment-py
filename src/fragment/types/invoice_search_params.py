# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "InvoiceSearchParams",
    "Filter",
    "FilterCreated",
    "FilterModified",
    "FilterTags",
    "FilterTagsAll",
    "FilterTagsAny",
    "FilterTransactionTags",
    "FilterTransactionTagsAll",
    "FilterTransactionTagsAny",
    "FilterUserTagAndBalance",
    "FilterUserTagAndBalanceNetRemainingBalance",
    "FilterUserTagAndBalanceUserTags",
    "FilterUserTagAndBalanceUserTagsAll",
    "FilterUserTagAndBalanceUserTagsAny",
    "FilterUserTagAndBalanceUserTagsNotAny",
    "FilterUsers",
    "FilterUsersAll",
    "FilterUsersAllID",
    "FilterUsersAllExternalID",
    "FilterUsersAny",
    "FilterUsersAnyID",
    "FilterUsersAnyExternalID",
    "PageInfo",
]


class InvoiceSearchParams(TypedDict, total=False):
    filter: Required[Filter]
    """Filter criteria for the search."""

    page_info: PageInfo
    """Pagination parameters."""


class FilterCreated(TypedDict, total=False):
    """Filter by invoice creation timestamp.

    When both `after` and `before` are provided, results must fall in the range.
    """

    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Returns invoices created at or after the timestamp. ISO 8601 datetime."""

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Returns invoices created at or before the timestamp. ISO 8601 datetime."""


class FilterModified(TypedDict, total=False):
    """Filter by invoice last modified timestamp.

    When both `after` and `before` are provided, results must fall in the range.
    """

    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Returns invoices last modified at or after the timestamp. ISO 8601 datetime."""

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Returns invoices last modified at or before the timestamp. ISO 8601 datetime."""


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
    """Returns invoices matching every specified tag, using AND logic."""

    any: Iterable[FilterTagsAny]
    """Returns invoices matching at least one of the specified tags, using OR logic."""


class FilterTransactionTagsAll(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterTransactionTagsAny(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterTransactionTags(TypedDict, total=False):
    """Filter invoices by tags on transactions allocated to them.

    Returns invoices that have at least one allocated transaction matching the specified tags.
    """

    all: Iterable[FilterTransactionTagsAll]
    """Returns transactions matching every specified tag, using AND logic."""

    any: Iterable[FilterTransactionTagsAny]
    """
    Returns transactions matching at least one of the specified tags, using OR
    logic.
    """


class FilterUserTagAndBalanceNetRemainingBalance(TypedDict, total=False):
    """Numeric comparator for the per-user net remaining balance on the invoice.

    Multiple keys combine with AND logic.
    """

    eq: str
    """Equal to.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """

    gt: str
    """Strictly greater than.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """

    gte: str
    """Greater than or equal to.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """

    lt: str
    """Strictly less than.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """

    lte: str
    """Less than or equal to.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """

    ne: str
    """Not equal to.

    Decimal integer string in the smallest currency unit, such as cents for USD.
    """


class FilterUserTagAndBalanceUserTagsAll(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterUserTagAndBalanceUserTagsAny(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterUserTagAndBalanceUserTagsNotAny(TypedDict, total=False):
    """A tag filter."""

    key: Required[str]
    """Tag key to filter on. Must be an exact match; wildcards are not supported."""

    value: Required[str]
    """Tag value pattern to filter on.

    Supports wildcards: `*` matches any characters, `?` matches a single character.
    Use `\\**` or `\\??` to match literal asterisks or question marks. Use `*` to match
    any value for the given key.
    """


class FilterUserTagAndBalanceUserTags(TypedDict, total=False):
    """Tag-based filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all` AND at least one entry in `any`.
    """

    all: Iterable[FilterUserTagAndBalanceUserTagsAll]
    """Returns users matching every specified tag, using AND logic."""

    any: Iterable[FilterUserTagAndBalanceUserTagsAny]
    """Returns users matching at least one of the specified tags, using OR logic."""

    not_any: Iterable[FilterUserTagAndBalanceUserTagsNotAny]
    """Returns users that do not match any of the specified tags."""


class FilterUserTagAndBalance(TypedDict, total=False):
    """
    Returns invoices where at least one line item user, optionally restricted to users matching `user_tags`, has a per-invoice net remaining balance satisfying `net_remaining_balance` on any currency. Pagination is disabled when this filter is set; any `page_info` provided in the request is ignored.
    """

    net_remaining_balance: Required[FilterUserTagAndBalanceNetRemainingBalance]
    """Numeric comparator for the per-user net remaining balance on the invoice.

    Multiple keys combine with AND logic.
    """

    user_tags: FilterUserTagAndBalanceUserTags
    """Tag-based filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all`
    AND at least one entry in `any`.
    """


class FilterUsersAllID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class FilterUsersAllExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


FilterUsersAll: TypeAlias = Union[FilterUsersAllID, FilterUsersAllExternalID]


class FilterUsersAnyID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class FilterUsersAnyExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


FilterUsersAny: TypeAlias = Union[FilterUsersAnyID, FilterUsersAnyExternalID]


class FilterUsers(TypedDict, total=False):
    """Line item user filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all` AND at least one entry in `any`.
    """

    all: Iterable[FilterUsersAll]
    """Returns invoices matching every specified line item user, using AND logic."""

    any: Iterable[FilterUsersAny]
    """
    Returns invoices matching at least one of the specified line item users, using
    OR logic.
    """


class Filter(TypedDict, total=False):
    """Filter criteria for the search."""

    created: FilterCreated
    """Filter by invoice creation timestamp.

    When both `after` and `before` are provided, results must fall in the range.
    """

    modified: FilterModified
    """Filter by invoice last modified timestamp.

    When both `after` and `before` are provided, results must fall in the range.
    """

    status: Literal["open"]
    """Filter by invoice status.

    `open` returns invoices with non-zero clearing account balances. Pagination is
    disabled when this filter is set; any `page_info` provided in the request is
    ignored.
    """

    tags: FilterTags
    """Tag-based filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all`
    AND at least one entry in `any`.
    """

    transaction_tags: FilterTransactionTags
    """Filter invoices by tags on transactions allocated to them.

    Returns invoices that have at least one allocated transaction matching the
    specified tags.
    """

    user_tag_and_balance: FilterUserTagAndBalance
    """
    Returns invoices where at least one line item user, optionally restricted to
    users matching `user_tags`, has a per-invoice net remaining balance satisfying
    `net_remaining_balance` on any currency. Pagination is disabled when this filter
    is set; any `page_info` provided in the request is ignored.
    """

    users: FilterUsers
    """Line item user filter criteria.

    When both `any` and `all` are provided, results must match every entry in `all`
    AND at least one entry in `any`.
    """


class PageInfo(TypedDict, total=False):
    """Pagination parameters."""

    after: str
    """Cursor for fetching the next page of results."""

    limit: int
    """Number of results to return. Defaults to 20."""
