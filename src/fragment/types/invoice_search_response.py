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
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceBalancePayins(BaseModel):
    actual: str
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceBalancePayouts(BaseModel):
    actual: str
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceBalance(BaseModel):
    currency: str
    """Currency code (ISO 4217 or crypto)."""

    net: DataInvoiceBalanceNet

    payins: DataInvoiceBalancePayins

    payouts: DataInvoiceBalancePayouts


class DataInvoicePaymentTransactionTag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class DataInvoicePaymentTransaction(BaseModel):
    """Transaction reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""

    tags: List[DataInvoicePaymentTransactionTag]
    """Tags from the parent transaction."""


class DataInvoicePaymentUser(BaseModel):
    """User reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class DataInvoicePayment(BaseModel):
    """A payment allocated to the invoice."""

    amount: str
    """
    Amount allocated as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

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
    """Currency code (ISO 4217 or crypto)."""

    posted: datetime
    """Timestamp when the parent transaction was posted. Uses ISO 8601 format."""

    transaction: DataInvoicePaymentTransaction
    """Transaction reference."""

    type: Literal["payin", "payout"]
    """Type of the payment."""

    user: DataInvoicePaymentUser
    """User reference."""


class DataInvoiceUserBalanceNet(BaseModel):
    actual: str
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceUserBalancePayins(BaseModel):
    actual: str
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceUserBalancePayouts(BaseModel):
    actual: str
    """
    Actual amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    expected: str
    """
    Expected amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """

    remaining: str
    """
    Remaining amount as a string in the smallest unit of the currency (for example,
    cents for USD).
    """


class DataInvoiceUserBalance(BaseModel):
    currency: str
    """Currency code (ISO 4217 or crypto)."""

    net: DataInvoiceUserBalanceNet

    payins: DataInvoiceUserBalancePayins

    payouts: DataInvoiceUserBalancePayouts


class DataInvoiceUser(BaseModel):
    id: str
    """User-provided unique external ID."""

    balances: List[DataInvoiceUserBalance]
    """Per-currency balance breakdown for the user."""

    external_id: str
    """User-provided unique ID."""


class DataInvoice(Invoice):
    """Invoice with balance details."""

    balances: List[DataInvoiceBalance]
    """Invoice-level balances by currency."""

    payments: List[DataInvoicePayment]
    """Payments allocated to the invoice."""

    users: List[DataInvoiceUser]
    """Users involved in the invoice."""


class DataPageInfo(BaseModel):
    """Pagination cursors."""

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page of results."""


class Data(BaseModel):
    invoices: List[DataInvoice]
    """Invoices matching the search criteria."""

    page_info: DataPageInfo
    """Pagination cursors."""


class InvoiceSearchResponse(BaseModel):
    """Search results for invoices."""

    data: Data
