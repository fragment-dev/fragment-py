# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InvoiceUpdateParams",
    "LineItems",
    "LineItemsCreate",
    "LineItemsCreateUser",
    "LineItemsCreateUserID",
    "LineItemsCreateUserExternalID",
    "LineItemsCreatePrice",
    "LineItemsCreateTag",
    "LineItemsDelete",
    "LineItemsUpdate",
    "LineItemsUpdatePrice",
    "LineItemsUpdateTags",
    "LineItemsUpdateTagsCreate",
    "LineItemsUpdateTagsDelete",
    "LineItemsUpdateTagsSet",
    "LineItemsUpdateTagsUpdate",
    "Tags",
    "TagsCreate",
    "TagsDelete",
    "TagsSet",
    "TagsUpdate",
]


class InvoiceUpdateParams(TypedDict, total=False):
    current_invoice_version: Required[float]
    """Current version of the invoice. Must match the stored version."""

    line_items: LineItems
    """Line item updates."""

    tags: Tags
    """Tag updates."""


class LineItemsCreateUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated unique ID."""


class LineItemsCreateUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique ID."""


LineItemsCreateUser: TypeAlias = Union[LineItemsCreateUserID, LineItemsCreateUserExternalID]


class LineItemsCreatePrice(TypedDict, total=False):
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


class LineItemsCreateTag(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class LineItemsCreate(TypedDict, total=False):
    """Data to create a line item."""

    description: Required[str]
    """Description of the line item."""

    product_id: Required[str]
    """Unique identifier for the product."""

    type: Required[Literal["payin", "payout"]]
    """Type of the line item."""

    user: Required[LineItemsCreateUser]
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

    price: LineItemsCreatePrice
    """Price breakdown. Provide amount, or unit_price and quantity, or all three."""

    tags: Iterable[LineItemsCreateTag]
    """Tags for the line item."""


class LineItemsDelete(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the line item to delete."""


class LineItemsUpdatePrice(TypedDict, total=False):
    quantity: Required[int]
    """Number of units for the line item."""

    unit_price: Required[str]
    """
    Price per unit as a string in the smallest currency unit, such as cents for USD.
    """

    amount: str
    """Total amount as a string in the smallest currency unit, such as cents for USD."""


class LineItemsUpdateTagsCreate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class LineItemsUpdateTagsDelete(TypedDict, total=False):
    key: Required[str]
    """Tag key to delete."""


class LineItemsUpdateTagsSet(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class LineItemsUpdateTagsUpdate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class LineItemsUpdateTags(TypedDict, total=False):
    """Tag updates."""

    create: Iterable[LineItemsUpdateTagsCreate]
    """Tags to create. The tag key must not already exist."""

    delete: Iterable[LineItemsUpdateTagsDelete]
    """Tags to remove."""

    set: Iterable[LineItemsUpdateTagsSet]
    """Tags to set. Creates a new tag or updates an existing tag."""

    update: Iterable[LineItemsUpdateTagsUpdate]
    """Tags to update. The tag key must already exist."""


class LineItemsUpdate(TypedDict, total=False):
    """Data for updating a line item."""

    id: Required[str]
    """Unique identifier for the line item to update."""

    description: str

    price: LineItemsUpdatePrice

    tags: LineItemsUpdateTags
    """Tag updates."""


class LineItems(TypedDict, total=False):
    """Line item updates."""

    create: Iterable[LineItemsCreate]
    """Line items to add to the invoice."""

    delete: Iterable[LineItemsDelete]
    """Line items to remove from the invoice."""

    update: Iterable[LineItemsUpdate]
    """Existing line items to update."""


class TagsCreate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsDelete(TypedDict, total=False):
    key: Required[str]
    """Tag key to delete."""


class TagsSet(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class TagsUpdate(TypedDict, total=False):
    """A key-value tag pair for metadata."""

    key: Required[str]
    """Tag key. Must not contain #, /, or :. Max 50 characters."""

    value: Required[str]
    """Tag value. Must not contain #, /, or :. Max 200 characters."""


class Tags(TypedDict, total=False):
    """Tag updates."""

    create: Iterable[TagsCreate]
    """Tags to create. The tag key must not already exist."""

    delete: Iterable[TagsDelete]
    """Tags to remove."""

    set: Iterable[TagsSet]
    """Tags to set. Creates a new tag or updates an existing tag."""

    update: Iterable[TagsUpdate]
    """Tags to update. The tag key must already exist."""
