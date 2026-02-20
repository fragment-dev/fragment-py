# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .invoice import Invoice
from .._models import BaseModel

__all__ = [
    "InvoiceRetrieveResponse",
    "Data",
    "DataBalance",
    "DataBalanceNet",
    "DataBalancePayins",
    "DataBalancePayouts",
    "DataUser",
    "DataUserBalance",
    "DataUserBalanceNet",
    "DataUserBalancePayins",
    "DataUserBalancePayouts",
]


class DataBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataBalanceNet

    payins: DataBalancePayins

    payouts: DataBalancePayouts


class DataUserBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataUserBalanceNet

    payins: DataUserBalancePayins

    payouts: DataUserBalancePayouts


class DataUser(BaseModel):
    id: str
    """User/party ID"""

    balances: List[DataUserBalance]
    """Per-currency balance breakdown for this user"""


class Data(Invoice):
    """Invoice with balance details"""

    balances: List[DataBalance]
    """Invoice-level balances by currency: payins, payouts, and net (payins - payouts)"""

    users: List[DataUser]
    """Users/parties involved in the invoice"""


class InvoiceRetrieveResponse(BaseModel):
    data: Data
    """Invoice with balance details"""
