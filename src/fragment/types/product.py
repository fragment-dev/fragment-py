# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Product", "PaidByRole", "PaidToRole"]


class PaidByRole(BaseModel):
    """Reference to a role by its unique ID"""

    id: str
    """The unique ID of the role"""

    name: str
    """The name of the role"""


class PaidToRole(BaseModel):
    """Reference to a role by its unique ID"""

    id: str
    """The unique ID of the role"""

    name: str
    """The name of the role"""


class Product(BaseModel):
    """Product object"""

    id: str
    """Unique identifier for the product"""

    code: str
    """User-defined product identifier."""

    created: datetime
    """ISO 8601 timestamp when the product was created"""

    description: str
    """Description of the product"""

    paid_by_roles: List[PaidByRole]
    """User roles that can pay for this product"""

    paid_to_roles: List[PaidToRole]
    """User roles that receive payment for this product"""

    update_version: float = FieldInfo(alias="updateVersion")
    """Version number for optimistic locking"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this product belongs to"""
