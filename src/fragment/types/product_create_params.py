# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "ProductCreateParams",
    "PaidByRole",
    "PaidByRoleID",
    "PaidByRoleName",
    "PaidToRole",
    "PaidToRoleID",
    "PaidToRoleName",
]


class ProductCreateParams(TypedDict, total=False):
    code: Required[str]
    """Unique product code."""

    description: str
    """Product description."""

    paid_by_roles: Iterable[PaidByRole]
    """Roles that can pay for the product.

    Reference roles by `id` or `name`. At least one of `paid_by_roles` or
    `paid_to_roles` must be provided.
    """

    paid_to_roles: Iterable[PaidToRole]
    """Roles that can receive payment for the product.

    Reference roles by `id` or `name`. At least one of `paid_by_roles` or
    `paid_to_roles` must be provided.
    """


class PaidByRoleID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class PaidByRoleName(TypedDict, total=False):
    name: Required[str]
    """Name of the role."""


PaidByRole: TypeAlias = Union[PaidByRoleID, PaidByRoleName]


class PaidToRoleID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class PaidToRoleName(TypedDict, total=False):
    name: Required[str]
    """Name of the role."""


PaidToRole: TypeAlias = Union[PaidToRoleID, PaidToRoleName]
