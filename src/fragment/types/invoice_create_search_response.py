# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .invoice import Invoice
from .._models import BaseModel

__all__ = ["InvoiceCreateSearchResponse", "Data", "DataPageInfo"]


class DataPageInfo(BaseModel):
    """Pagination cursors."""

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page of results"""


class Data(BaseModel):
    invoices: List[Invoice]
    """List of invoices matching the search criteria"""

    page_info: DataPageInfo
    """Pagination cursors."""


class InvoiceCreateSearchResponse(BaseModel):
    """Response body for searching invoices"""

    data: Data
