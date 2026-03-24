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
    """Account reference. Provide id, external_id, or both."""

    allocations: Required[Iterable[Allocation]]
    """Allocation entries for this transaction. Empty indicates unreconciled funds."""

    amount: Required[str]
    """
    Amount in smallest currency unit as stringified bigint (can be positive or
    negative).
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
    """Currency code (ISO 4217 or crypto)"""

    external_id: Required[str]
    """External transaction ID used for idempotent sync."""

    posted: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Posted timestamp in ISO 8601 format."""

    tags: Iterable[Tag]
    """Optional metadata tags for this transaction"""


class Account(TypedDict, total=False):
    """Account reference. Provide id, external_id, or both."""

    id: str
    """User-facing encoded account ID."""

    external_id: str
    """External account reference ID."""


class AllocationUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated ID of the user"""


class AllocationUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user"""


AllocationUser: TypeAlias = Union[AllocationUserID, AllocationUserExternalID]


class Allocation(TypedDict, total=False):
    """Transaction allocation against an invoice."""

    amount: Required[str]
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: Required[str]
    """The invoice to allocate against."""

    type: Required[Literal["invoice_payin", "invoice_payout"]]
    """The type of allocation."""

    user: Required[AllocationUser]
    """Identifies a user by Fragment-generated id or external_id (request body)."""


class Tag(TypedDict, total=False):
    """A key-value tag pair for metadata"""

    key: Required[str]
    """Tag key.

    Must be a valid safe string (no special characters like #, /, :). Max 50
    characters.
    """

    value: Required[str]
    """Tag value.

    Must be a valid safe string (no special characters like #, /, :). Max 200
    characters.
    """
