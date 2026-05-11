# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProductCreateParams"]


class ProductCreateParams(TypedDict, total=False):
    code: Required[str]
    """Unique product code."""

    description: str
    """Product description."""
