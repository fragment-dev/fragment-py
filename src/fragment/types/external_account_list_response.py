# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .external_account import ExternalAccount

__all__ = ["ExternalAccountListResponse"]


class ExternalAccountListResponse(BaseModel):
    """List of external accounts"""

    data: List[ExternalAccount]
