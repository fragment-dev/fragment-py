# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .platform import Platform

__all__ = ["PlatformUpdateResponse"]


class PlatformUpdateResponse(BaseModel):
    data: Platform
    """Platform object"""
