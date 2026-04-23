# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .role import Role
from .._models import BaseModel

__all__ = ["RoleCreateResponse"]


class RoleCreateResponse(BaseModel):
    data: Role
    """Role object. Deprecated, use user tags instead."""
