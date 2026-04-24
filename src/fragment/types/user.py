# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["User", "Tag"]


class Tag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class User(BaseModel):
    """User object."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""

    role: str
    """Name of the user's role. Deprecated, use tags instead."""

    tags: List[Tag]
    """Tags for the user."""
