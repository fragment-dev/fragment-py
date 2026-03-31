# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["TransactionSearchResponse"]


class TransactionSearchResponse(BaseModel):
    """Search results for transactions."""

    data: List[Transaction]
