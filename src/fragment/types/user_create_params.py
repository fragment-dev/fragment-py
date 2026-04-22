# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams", "Tag"]


class UserCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""

    role: Required[str]
    """Name of the role to assign. Must match an existing role."""

    tags: Iterable[Tag]
    """Tags for the user."""


class Tag(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""
