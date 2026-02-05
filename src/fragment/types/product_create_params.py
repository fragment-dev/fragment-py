# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "ProductCreateParams",
    "PaidByRole",
    "PaidByRoleRoleMatchByID",
    "PaidByRoleRoleMatchByName",
    "PaidToRole",
    "PaidToRoleRoleMatchByID",
    "PaidToRoleRoleMatchByName",
]


class ProductCreateParams(TypedDict, total=False):
    code: Required[str]
    """Product code (unique identifier)"""

    description: Required[str]
    """Description of the product"""

    paid_by_roles: Iterable[PaidByRole]
    """Roles that can pay for this product.

    Reference roles by id or name. At least one of paid_by_roles or paid_to_roles
    must be provided.
    """

    paid_to_roles: Iterable[PaidToRole]
    """Roles that receive payment for this product.

    Reference roles by id or name. At least one of paid_by_roles or paid_to_roles
    must be provided.
    """


class PaidByRoleRoleMatchByID(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the role"""


class PaidByRoleRoleMatchByName(TypedDict, total=False):
    name: Required[str]
    """The name of the role"""


PaidByRole: TypeAlias = Union[PaidByRoleRoleMatchByID, PaidByRoleRoleMatchByName]


class PaidToRoleRoleMatchByID(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the role"""


class PaidToRoleRoleMatchByName(TypedDict, total=False):
    name: Required[str]
    """The name of the role"""


PaidToRole: TypeAlias = Union[PaidToRoleRoleMatchByID, PaidToRoleRoleMatchByName]
