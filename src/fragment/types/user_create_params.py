# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    role: Required[str]
    """Role of the user"""

    body_external_id_1: Annotated[str, PropertyInfo(alias="external_id")]
    """External ID for the user"""

    body_external_id_2: Annotated[str, PropertyInfo(alias="externalId")]
    """External ID for the user"""
