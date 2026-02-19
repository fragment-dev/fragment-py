# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .platform import Platform

__all__ = ["PlatformRetrieveResponse"]


class PlatformRetrieveResponse(BaseModel):
    data: Platform
    """Platform object"""
