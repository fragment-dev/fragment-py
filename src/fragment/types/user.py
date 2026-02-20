# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    """User object"""

    id: str
    """Unique user ID"""

    external_id: str = FieldInfo(alias="externalId")
    """External ID for the user"""

    role: str
    """Role of the user"""
