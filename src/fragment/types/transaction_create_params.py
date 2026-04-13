# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TransactionCreateParams",
    "Account",
    "Allocation",
    "AllocationUser",
    "AllocationUserID",
    "AllocationUserExternalID",
    "Tag",
]


class TransactionCreateParams(TypedDict, total=False):
    account: Required[Account]
    """External account for the transaction.

    Identify it by `id`, `external_id`, or both.
    """

    allocations: Required[Iterable[Allocation]]
    """Allocations for the transaction. An empty array indicates unreconciled funds."""

    amount: Required[str]
    """
    Transaction amount, as a string in the smallest currency unit, such as cents for
    USD. Can be positive or negative.
    """

    currency: Required[
        Literal[
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
    ]
    """ISO 4217 or crypto currency code."""

    external_id: Required[str]
    """User-provided unique ID."""

    posted: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp when the transaction was posted. Uses ISO 8601 format."""

    tags: Iterable[Tag]
    """Tags for the transaction."""


class Account(TypedDict, total=False):
    """External account for the transaction.

    Identify it by `id`, `external_id`, or both.
    """

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class AllocationUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class AllocationUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


AllocationUser: TypeAlias = Union[AllocationUserID, AllocationUserExternalID]


class Allocation(TypedDict, total=False):
    """An allocation linking a transaction to an invoice."""

    amount: Required[str]
    """
    Allocation amount, as a positive string in the smallest currency unit, such as
    cents for USD.
    """

    invoice_id: Required[str]
    """Invoice to allocate against."""

    type: Required[Literal["invoice_payin", "invoice_payout"]]
    """Type of allocation."""

    user: Required[AllocationUser]
    """Identifies a user by `id` or `external_id`."""


class Tag(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""
