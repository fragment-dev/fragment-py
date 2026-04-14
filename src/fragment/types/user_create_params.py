# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""

    role: Required[str]
    """Name of the role to assign. Must match an existing role."""
