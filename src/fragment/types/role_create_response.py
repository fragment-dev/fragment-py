# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RoleCreateResponse", "Data"]


class Data(BaseModel):
    """Role object"""

    id: str
    """Unique role ID"""

    role: str
    """Name of the role"""


class RoleCreateResponse(BaseModel):
    data: Data
    """Role object"""
