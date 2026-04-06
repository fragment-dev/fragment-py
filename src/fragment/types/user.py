# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    """User object."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique external ID."""

    role: str
    """Name of the user's role."""
