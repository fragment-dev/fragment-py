# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .invoice import Invoice
from .._models import BaseModel

__all__ = [
    "InvoiceRetrieveResponse",
    "Data",
    "DataBalance",
    "DataBalanceNet",
    "DataBalancePayins",
    "DataBalancePayouts",
    "DataPayment",
    "DataPaymentTransaction",
    "DataPaymentTransactionTag",
    "DataPaymentUser",
    "DataUser",
    "DataUserBalance",
    "DataUserBalanceNet",
    "DataUserBalancePayins",
    "DataUserBalancePayouts",
]


class DataBalanceNet(BaseModel):
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


class DataBalancePayins(BaseModel):
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


class DataBalancePayouts(BaseModel):
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


class DataBalance(BaseModel):
    currency: str
    """Currency code (ISO 4217 or crypto)."""

    net: DataBalanceNet

    payins: DataBalancePayins

    payouts: DataBalancePayouts


class DataPaymentTransactionTag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class DataPaymentTransaction(BaseModel):
    """Transaction reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""

    tags: List[DataPaymentTransactionTag]
    """Tags from the parent transaction."""


class DataPaymentUser(BaseModel):
    """User reference."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class DataPayment(BaseModel):
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

    transaction: DataPaymentTransaction
    """Transaction reference."""

    type: Literal["payin", "payout"]
    """Type of the payment."""

    user: DataPaymentUser
    """User reference."""


class DataUserBalanceNet(BaseModel):
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


class DataUserBalancePayins(BaseModel):
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


class DataUserBalancePayouts(BaseModel):
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


class DataUserBalance(BaseModel):
    currency: str
    """Currency code (ISO 4217 or crypto)."""

    net: DataUserBalanceNet

    payins: DataUserBalancePayins

    payouts: DataUserBalancePayouts


class DataUser(BaseModel):
    id: str
    """User-provided unique external ID."""

    balances: List[DataUserBalance]
    """Per-currency balance breakdown for the user."""

    external_id: str
    """User-provided unique ID."""


class Data(Invoice):
    """Invoice with balance details."""

    balances: List[DataBalance]
    """Invoice-level balances by currency."""

    payments: List[DataPayment]
    """Payments allocated to the invoice."""

    users: List[DataUser]
    """Users involved in the invoice."""


class InvoiceRetrieveResponse(BaseModel):
    data: Data
    """Invoice with balance details."""
