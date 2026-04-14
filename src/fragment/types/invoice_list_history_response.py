# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .invoice import Invoice
from .._models import BaseModel

__all__ = ["InvoiceListHistoryResponse"]


class InvoiceListHistoryResponse(BaseModel):
    data: List[Invoice]
    """Version history of the invoice."""
