# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .invoice import Invoice
from .._models import BaseModel

__all__ = ["InvoiceListResponse"]


class InvoiceListResponse(BaseModel):
    """List of invoices"""

    data: List[Invoice]
