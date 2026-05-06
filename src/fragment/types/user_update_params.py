# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateParams", "Tags", "TagsCreate", "TagsDelete", "TagsSet", "TagsUpdate"]


class UserUpdateParams(TypedDict, total=False):
    tags: Required[Tags]
    """Tag updates."""


class TagsCreate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsDelete(TypedDict, total=False):
    key: Required[str]
    """Tag key to delete."""


class TagsSet(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsUpdate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class Tags(TypedDict, total=False):
    """Tag updates."""

    create: Iterable[TagsCreate]
    """Tags to create. The tag key must not already exist."""

    delete: Iterable[TagsDelete]
    """Tags to remove."""

    set: Iterable[TagsSet]
    """Tags to set. Creates a new tag or updates an existing tag."""

    update: Iterable[TagsUpdate]
    """Tags to update. The tag key must already exist."""
