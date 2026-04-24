# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentSearchParams", "PageInfo"]


class PaymentSearchParams(TypedDict, total=False):
    page_info: PageInfo
    """Pagination parameters."""

    payment_flow_id: str
    """Filter by payment flow ID."""


class PageInfo(TypedDict, total=False):
    """Pagination parameters."""

    after: str
    """Pagination cursor."""

    limit: float
    """Maximum number of results."""
