# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentFlowSearchParams", "PageInfo"]


class PaymentFlowSearchParams(TypedDict, total=False):
    invoice_id: str
    """Filter by invoice ID."""

    page_info: PageInfo
    """Pagination parameters."""


class PageInfo(TypedDict, total=False):
    """Pagination parameters."""

    after: str
    """Pagination cursor."""

    limit: float
    """Maximum number of results."""
