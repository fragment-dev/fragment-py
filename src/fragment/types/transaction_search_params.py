# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TransactionSearchParams", "Filter", "FilterAccount", "FilterAccountAny"]


class TransactionSearchParams(TypedDict, total=False):
    filter: Required[Filter]
    """Filter for searching transactions."""


class FilterAccountAny(TypedDict, total=False):
    """External account for the transaction.

    Identify it by `id`, `external_id`, or both.
    """

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """Unique user-provided external ID for the external account."""


class FilterAccount(TypedDict, total=False):
    any: Required[Iterable[FilterAccountAny]]
    """Match transactions belonging to any of these accounts (OR)."""


class Filter(TypedDict, total=False):
    """Filter for searching transactions."""

    account: Required[FilterAccount]
