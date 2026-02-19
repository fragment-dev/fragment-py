# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
    """External account object"""

    id: str
    """Fragment-generated unique ID for the external account"""

    external_id: str
    """User-provided external ID"""

    name: str
    """Human-readable name for the external account"""
