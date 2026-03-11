# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TransactionSearchParams", "Filter", "FilterInvoiceID"]


class TransactionSearchParams(TypedDict, total=False):
    filter: Required[Filter]
    """Filter criteria for searching transaction allocations."""


class FilterInvoiceID(TypedDict, total=False):
    any: Required[SequenceNotStr[str]]
    """Match allocations where invoice_id is any of these values (OR)."""


class Filter(TypedDict, total=False):
    """Filter criteria for searching transaction allocations."""

    invoice_id: Required[FilterInvoiceID]
