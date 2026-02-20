# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalAccountCreateParams"]


class ExternalAccountCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """External ID for the account (user-provided, unique, mutable)"""

    name: Required[str]
    """Human-readable name for the external account (mutable)"""
