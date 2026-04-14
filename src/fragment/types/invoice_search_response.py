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
    """Net balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceBalancePayins(BaseModel):
    """Payins balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceBalancePayouts(BaseModel):
    """Payouts balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceBalance(BaseModel):
    currency: str
    """ISO 4217 or crypto currency code."""

    net: DataInvoiceBalanceNet
    """Net balance breakdown."""

    payins: DataInvoiceBalancePayins
    """Payins balance breakdown."""

    payouts: DataInvoiceBalancePayouts
    """Payouts balance breakdown."""


class DataInvoicePaymentTransactionTag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class DataInvoicePaymentTransaction(BaseModel):
    """Transaction the payment is applied to."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""

    tags: List[DataInvoicePaymentTransactionTag]
    """Tags from the parent transaction."""


class DataInvoicePaymentUser(BaseModel):
    """User associated with the payment."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class DataInvoicePayment(BaseModel):
    """A payment allocated to the invoice."""

    amount: str
    """
    Amount allocated as a string in the smallest currency unit, such as cents for
    USD.
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
    """ISO 4217 or crypto currency code."""

    posted: datetime
    """Timestamp when the parent transaction was posted. Uses ISO 8601 format."""

    transaction: DataInvoicePaymentTransaction
    """Transaction the payment is applied to."""

    type: Literal["payin", "payout"]
    """Type of the payment."""

    user: DataInvoicePaymentUser
    """User associated with the payment."""


class DataInvoiceUserBalanceNet(BaseModel):
    """Net balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceUserBalancePayins(BaseModel):
    """Payins balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceUserBalancePayouts(BaseModel):
    """Payouts balance breakdown."""

    actual: str
    """Actual amount as a string in the smallest currency unit, such as cents for USD."""

    expected: str
    """
    Expected amount as a string in the smallest currency unit, such as cents for
    USD.
    """

    remaining: str
    """
    Remaining amount as a string in the smallest currency unit, such as cents for
    USD.
    """


class DataInvoiceUserBalance(BaseModel):
    currency: str
    """ISO 4217 or crypto currency code."""

    net: DataInvoiceUserBalanceNet
    """Net balance breakdown."""

    payins: DataInvoiceUserBalancePayins
    """Payins balance breakdown."""

    payouts: DataInvoiceUserBalancePayouts
    """Payouts balance breakdown."""


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
    """Search results for invoices."""

    invoices: List[DataInvoice]
    """Invoices matching the search criteria."""

    page_info: DataPageInfo
    """Pagination cursors."""


class InvoiceSearchResponse(BaseModel):
    """Search results for invoices."""

    data: Data
    """Search results for invoices."""
