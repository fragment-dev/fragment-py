# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductCreateParams", "Seller", "SellerPlatformSeller", "SellerUserSeller"]


class ProductCreateParams(TypedDict, total=False):
    code: Required[str]
    """Product code (unique identifier)"""

    description: Required[str]
    """Description of the product"""

    seller: Required[Seller]
    """Seller information"""


class SellerPlatformSeller(TypedDict, total=False):
    sold_by_platform: Required[Annotated[Literal[True], PropertyInfo(alias="soldByPlatform")]]
    """Indicates the product is sold by the platform"""


class SellerUserSeller(TypedDict, total=False):
    role: Required[str]
    """Role of the user"""

    sold_by_platform: Required[Annotated[Literal[False], PropertyInfo(alias="soldByPlatform")]]
    """Indicates the product is sold by a user"""


Seller: TypeAlias = Union[SellerPlatformSeller, SellerUserSeller]
