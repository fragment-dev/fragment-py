# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RoleListResponse", "Data"]


class Data(BaseModel):
    """Role object"""

    id: str
    """Unique role ID"""

    role: str
    """Name of the role"""


class RoleListResponse(BaseModel):
    """List of roles"""

    data: List[Data]
