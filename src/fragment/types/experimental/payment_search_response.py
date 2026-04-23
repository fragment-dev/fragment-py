# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .payment import Payment
from ..._models import BaseModel

__all__ = ["PaymentSearchResponse"]


class PaymentSearchResponse(BaseModel):
    """List of payments."""

    data: List[Payment]
