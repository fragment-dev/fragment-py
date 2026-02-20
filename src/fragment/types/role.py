# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    """Role object"""

    id: str
    """Unique role ID"""

    role: str
    """Name of the role"""
