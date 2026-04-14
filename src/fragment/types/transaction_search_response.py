# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["TransactionSearchResponse", "DataV2", "DataV2PageInfo"]


class DataV2PageInfo(BaseModel):
    """Pagination cursors."""

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page of results."""


class DataV2(BaseModel):
    page_info: DataV2PageInfo
    """Pagination cursors."""

    transactions: List[Transaction]
    """Transactions matching the search criteria."""


class TransactionSearchResponse(BaseModel):
    data: List[Transaction]
    """Deprecated.

    Use `data_v2.transactions` instead. Returns the full unpaginated list of
    matching transactions.
    """

    data_v2: DataV2
