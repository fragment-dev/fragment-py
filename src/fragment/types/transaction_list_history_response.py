# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["TransactionListHistoryResponse"]


class TransactionListHistoryResponse(BaseModel):
    data: List[Transaction]
    """List of transaction versions over time, ordered by version, oldest first."""
