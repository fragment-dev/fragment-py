# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveResponse", "Data", "DataSeller", "DataSellerPlatformSeller", "DataSellerUserSeller"]


class DataSellerPlatformSeller(BaseModel):
    sold_by_platform: Literal[True] = FieldInfo(alias="soldByPlatform")
    """Indicates the product is sold by the platform"""


class DataSellerUserSeller(BaseModel):
    role: str
    """Role of the user"""

    sold_by_platform: Literal[False] = FieldInfo(alias="soldByPlatform")
    """Indicates the product is sold by a user"""


DataSeller: TypeAlias = Union[DataSellerPlatformSeller, DataSellerUserSeller]


class Data(BaseModel):
    """Product object"""

    code: str
    """Product code (unique identifier)"""

    created: datetime
    """ISO 8601 timestamp when the product was created"""

    description: str
    """Description of the product"""

    seller: DataSeller
    """Seller information"""

    update_version: float = FieldInfo(alias="updateVersion")
    """Version number for optimistic locking"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this product belongs to"""


class ProductRetrieveResponse(BaseModel):
    data: Data
    """Product object"""
