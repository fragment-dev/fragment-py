# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .external_account import ExternalAccount

__all__ = ["ExternalAccountCreateResponse"]


class ExternalAccountCreateResponse(BaseModel):
    data: ExternalAccount
    """External account object"""
