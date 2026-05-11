# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Product"]


class Product(BaseModel):
    """Product object."""

    id: str
    """FRAGMENT generated unique ID."""

    code: str
    """Product code."""

    created: datetime
    """Timestamp when the product was created. Uses ISO 8601 format."""

    update_version: float
    """Current version of the product."""

    workspace_id: str
    """Workspace ID of the product."""

    description: Optional[str] = None
    """Product description."""
