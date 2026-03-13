# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InvoiceCreateParams",
    "LineItem",
    "LineItemUser",
    "LineItemUserID",
    "LineItemUserExternalID",
    "LineItemTag",
    "Tag",
]


class InvoiceCreateParams(TypedDict, total=False):
    invoice_id: Required[str]
    """Unique identifier for the invoice.

    Make this the canonical ID from your system for the transaction.
    """

    line_items: Required[Iterable[LineItem]]
    """List of line items to create with the invoice"""

    tags: Iterable[Tag]
    """Optional metadata tags for this invoice"""


class LineItemUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated ID of the user"""


class LineItemUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user"""


LineItemUser: TypeAlias = Union[LineItemUserID, LineItemUserExternalID]


class LineItemTag(TypedDict, total=False):
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


class LineItem(TypedDict, total=False):
    """Line item data for creating within an invoice."""

    amount: Required[str]
    """Amount in smallest currency unit (e.g., cents)"""

    description: Required[str]
    """Description of the line item"""

    product_id: Required[str]
    """ID of the product/catalog item"""

    type: Required[Literal["payin", "payout"]]
    """The type of the line item"""

    user: Required[LineItemUser]

    currency_code: Literal[
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

    tags: Iterable[LineItemTag]
    """Optional metadata tags for this line item"""


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
