# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
    """External account object."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """Unique user-provided external ID."""

    name: str
    """Human-readable name."""
