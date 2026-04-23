# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .role import Role
from .._models import BaseModel

__all__ = ["RoleListResponse"]


class RoleListResponse(BaseModel):
    """List of roles. Deprecated, use user tags instead."""

    data: List[Role]
    """List of roles. Deprecated, use user tags instead."""
