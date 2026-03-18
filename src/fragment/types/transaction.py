# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Transaction", "Account", "Allocation", "AllocationUser", "Tag"]


class Account(BaseModel):
    id: str
    """User-facing encoded account ID."""

    external_id: str
    """External account reference ID."""


class AllocationUser(BaseModel):
    id: str
    """FRAGMENT generated ID of the user"""

    external_id: Optional[str] = None
    """External ID of the user"""


class Allocation(BaseModel):
    """Transaction allocation against an invoice."""

    amount: str
    """Amount to allocate in smallest currency unit as stringified bigint."""

    invoice_id: str
    """The invoice to allocate against."""

    type: Literal["invoice_payin", "invoice_payout"]
    """The type of allocation."""

    user: AllocationUser


class Tag(BaseModel):
    """A key-value tag pair"""

    key: str
    """Tag key"""

    value: str
    """Tag value"""


class Transaction(BaseModel):
    """Transaction object."""

    id: str
    """User-facing encoded transaction ID."""

    account: Account

    allocations: List[Allocation]

    amount: str
    """
    Amount in smallest currency unit as stringified bigint (can be positive or
    negative).
    """

    created: datetime
    """Creation timestamp."""

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

    external_id: str
    """External idempotency key provided by the user."""

    posted: datetime
    """Posted timestamp in ISO 8601 format."""

    tags: List[Tag]
    """Metadata tags associated with this transaction."""

    unallocated_amount: str
    """Read-only amount not yet allocated."""

    version: int
    """Current version of the transaction, used for optimistic concurrency control."""

    modified: Optional[datetime] = None
    """Last modified timestamp."""
