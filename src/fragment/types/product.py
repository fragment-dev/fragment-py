# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Product", "PaidByRole", "PaidToRole"]


class PaidByRole(BaseModel):
    """Role reference in product API responses. Deprecated."""

    id: str
    """FRAGMENT generated unique ID."""

    name: str
    """Name of the role."""


class PaidToRole(BaseModel):
    """Role reference in product API responses. Deprecated."""

    id: str
    """FRAGMENT generated unique ID."""

    name: str
    """Name of the role."""


class Product(BaseModel):
    """Product object."""

    id: str
    """FRAGMENT generated unique ID."""

    code: str
    """Product code."""

    created: datetime
    """Timestamp when the product was created. Uses ISO 8601 format."""

    paid_by_roles: List[PaidByRole]
    """Deprecated. Roles that can pay for the product."""

    paid_to_roles: List[PaidToRole]
    """Deprecated. Roles that can receive payment for the product."""

    update_version: float
    """Current version of the product."""

    workspace_id: str
    """Workspace ID of the product."""

    description: Optional[str] = None
    """Product description."""
