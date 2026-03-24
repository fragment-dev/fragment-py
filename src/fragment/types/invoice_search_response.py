# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .invoice import Invoice
from .._models import BaseModel

__all__ = [
    "InvoiceSearchResponse",
    "Data",
    "DataInvoice",
    "DataInvoiceBalance",
    "DataInvoiceBalanceNet",
    "DataInvoiceBalancePayins",
    "DataInvoiceBalancePayouts",
    "DataInvoicePayment",
    "DataInvoicePaymentTransaction",
    "DataInvoicePaymentTransactionTag",
    "DataInvoicePaymentUser",
    "DataInvoiceUser",
    "DataInvoiceUserBalance",
    "DataInvoiceUserBalanceNet",
    "DataInvoiceUserBalancePayins",
    "DataInvoiceUserBalancePayouts",
    "DataPageInfo",
]


class DataInvoiceBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataInvoiceBalanceNet

    payins: DataInvoiceBalancePayins

    payouts: DataInvoiceBalancePayouts


class DataInvoicePaymentTransactionTag(BaseModel):
    """A key-value tag pair"""

    key: str
    """Tag key"""

    value: str
    """Tag value"""


class DataInvoicePaymentTransaction(BaseModel):
    """Reference to a transaction by encoded ID and external ID."""

    id: str
    """Encoded transaction ID."""

    external_id: str
    """External transaction ID."""

    tags: List[DataInvoicePaymentTransactionTag]
    """Metadata tags from the parent transaction."""


class DataInvoicePaymentUser(BaseModel):
    """User reference in API responses: Fragment user id and optional external_id."""

    id: str
    """FRAGMENT generated ID of the user"""

    external_id: Optional[str] = None
    """External ID of the user"""


class DataInvoicePayment(BaseModel):
    """A payment allocated to this invoice."""

    amount: str
    """Amount allocated in smallest currency unit as stringified bigint."""

    currency: Literal[
        "ADA",
        "BTC",
        "DAI",
        "ETH",
        "SOL",
        "USDC",
        "USDT",
        "USDG",
        "EURC",
        "CADC",
        "CADT",
        "XLM",
        "UNI",
        "BCH",
        "LTC",
        "AAVE",
        "LINK",
        "MATIC",
        "PTS",
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLL",
        "SOS",
        "SPL",
        "SRD",
        "SVC",
        "SYP",
        "STN",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TVD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
        "LOGICAL",
        "CUSTOM",
    ]
    """Currency code (ISO 4217 or crypto)"""

    posted: datetime
    """Posted timestamp of the parent transaction in ISO 8601 format."""

    transaction: DataInvoicePaymentTransaction
    """Reference to a transaction by encoded ID and external ID."""

    type: Literal["payin", "payout"]
    """The type of the payment."""

    user: DataInvoicePaymentUser
    """User reference in API responses: Fragment user id and optional external_id."""


class DataInvoiceUserBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceUserBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceUserBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataInvoiceUserBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataInvoiceUserBalanceNet

    payins: DataInvoiceUserBalancePayins

    payouts: DataInvoiceUserBalancePayouts


class DataInvoiceUser(BaseModel):
    id: str
    """User/party ID"""

    balances: List[DataInvoiceUserBalance]
    """Per-currency balance breakdown for this user"""


class DataInvoice(Invoice):
    """Invoice with balance details"""

    balances: List[DataInvoiceBalance]
    """Invoice-level balances by currency: payins, payouts, and net (payins - payouts)"""

    payments: List[DataInvoicePayment]
    """Transaction allocations (payments) associated with this invoice."""

    users: List[DataInvoiceUser]
    """Users/parties involved in the invoice"""


class DataPageInfo(BaseModel):
    """Pagination cursors."""

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page of results"""


class Data(BaseModel):
    invoices: List[DataInvoice]
    """List of invoices matching the search criteria"""

    page_info: DataPageInfo
    """Pagination cursors."""


class InvoiceSearchResponse(BaseModel):
    """Response body for searching invoices"""

    data: Data
