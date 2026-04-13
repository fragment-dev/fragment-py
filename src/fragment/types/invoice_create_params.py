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
    "LineItemPrice",
    "LineItemTag",
    "Tag",
]


class InvoiceCreateParams(TypedDict, total=False):
    invoice_id: Required[str]
    """Unique ID for the invoice."""

    line_items: Required[Iterable[LineItem]]
    """Line items to create with the invoice."""

    tags: Iterable[Tag]
    """Tags for the invoice."""


class LineItemUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class LineItemUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


LineItemUser: TypeAlias = Union[LineItemUserID, LineItemUserExternalID]


class LineItemPrice(TypedDict, total=False):
    """Price breakdown. Provide amount, or unit_price and quantity, or all three."""

    amount: str
    """Total amount as a string in the smallest currency unit, such as cents for USD.

    Required if unit_price and quantity are not provided.
    """

    quantity: int
    """Number of units for the line item."""

    unit_price: str
    """
    Price per unit as a string in the smallest currency unit, such as cents for USD.
    """


class LineItemTag(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class LineItem(TypedDict, total=False):
    """Data to create a line item."""

    description: Required[str]
    """Description of the line item."""

    product_id: Required[str]
    """Unique identifier for the product."""

    type: Required[Literal["payin", "payout"]]
    """Type of the line item."""

    user: Required[LineItemUser]
    """Identifies a user by `id` or `external_id`."""

    amount: str
    """Total amount as a string in the smallest currency unit, such as cents for USD.

    Deprecated, use price instead.
    """

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
    """ISO 4217 or crypto currency code."""

    price: LineItemPrice
    """Price breakdown. Provide amount, or unit_price and quantity, or all three."""

    tags: Iterable[LineItemTag]
    """Tags for the line item."""


class Tag(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""
