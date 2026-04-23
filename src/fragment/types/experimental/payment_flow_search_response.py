# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .payment_flow import PaymentFlow

__all__ = ["PaymentFlowSearchResponse"]


class PaymentFlowSearchResponse(BaseModel):
    """List of payment flows."""

    data: List[PaymentFlow]
