# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .payment_flow import PaymentFlow

__all__ = ["PaymentFlowCreateResponse"]


class PaymentFlowCreateResponse(BaseModel):
    data: PaymentFlow
    """Payment flow object."""
