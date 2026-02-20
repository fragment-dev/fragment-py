# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transaction import Transaction

__all__ = ["TransactionCreateResponse"]


class TransactionCreateResponse(BaseModel):
    data: Transaction
    """Transaction object."""
