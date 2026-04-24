# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    """Role object. Deprecated, use user tags instead."""

    id: str
    """FRAGMENT generated unique ID. Deprecated."""

    role: str
    """Name of the role. Deprecated, use user tags instead."""
