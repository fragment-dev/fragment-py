# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveResponse", "Data", "DataPaidByRole", "DataPaidToRole"]


class DataPaidByRole(BaseModel):
    """Reference to a role by its unique ID"""

    id: str
    """The unique ID of the role"""

    name: str
    """The name of the role"""


class DataPaidToRole(BaseModel):
    """Reference to a role by its unique ID"""

    id: str
    """The unique ID of the role"""

    name: str
    """The name of the role"""


class Data(BaseModel):
    """Product object"""

    id: str
    """Unique identifier for the product"""

    code: str
    """User-defined product identifier."""

    created: datetime
    """ISO 8601 timestamp when the product was created"""

    description: str
    """Description of the product"""

    paid_by_roles: List[DataPaidByRole]
    """User roles that can pay for this product"""

    paid_to_roles: List[DataPaidToRole]
    """User roles that receive payment for this product"""

    update_version: float = FieldInfo(alias="updateVersion")
    """Version number for optimistic locking"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this product belongs to"""


class ProductRetrieveResponse(BaseModel):
    data: Data
    """Product object"""
