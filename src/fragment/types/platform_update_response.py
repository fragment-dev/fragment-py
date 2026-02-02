# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PlatformUpdateResponse", "Data"]


class Data(BaseModel):
    """Platform object"""

    created: datetime
    """ISO 8601 timestamp when the platform was created"""

    display_name: str = FieldInfo(alias="displayName")
    """Display name for the platform"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this platform belongs to"""

    modified: Optional[datetime] = None
    """ISO 8601 timestamp when the platform was last modified"""


class PlatformUpdateResponse(BaseModel):
    data: Data
    """Platform object"""
