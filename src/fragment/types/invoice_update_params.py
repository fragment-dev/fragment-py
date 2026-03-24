# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InvoiceUpdateParams",
    "LineItemsUpdate",
    "LineItemsUpdateAddLineItemOperation",
    "LineItemsUpdateAddLineItemOperationUser",
    "LineItemsUpdateAddLineItemOperationUserID",
    "LineItemsUpdateAddLineItemOperationUserExternalID",
    "LineItemsUpdateAddLineItemOperationPrice",
    "LineItemsUpdateAddLineItemOperationTag",
    "LineItemsUpdateUpdateLineItemOperation",
    "LineItemsUpdateUpdateLineItemOperationPrice",
    "LineItemsUpdateDeleteLineItemOperation",
]


class InvoiceUpdateParams(TypedDict, total=False):
    line_items_update: Required[Iterable[LineItemsUpdate]]
    """List of line item operations to apply to the invoice"""

    version: Required[float]
    """The version of the invoice being updated.

    Must match the current version for the update to succeed.
    """


class LineItemsUpdateAddLineItemOperationUserID(TypedDict, total=False):
    id: Required[str]
    """FRAGMENT generated ID of the user"""


class LineItemsUpdateAddLineItemOperationUserExternalID(TypedDict, total=False):
    external_id: Required[str]
    """External ID of the user"""


LineItemsUpdateAddLineItemOperationUser: TypeAlias = Union[
    LineItemsUpdateAddLineItemOperationUserID, LineItemsUpdateAddLineItemOperationUserExternalID
]


class LineItemsUpdateAddLineItemOperationPrice(TypedDict, total=False):
    """Price breakdown. Provide amount, or unit_price + quantity, or all three."""

    amount: str
    """Total amount in smallest currency unit.

    Required if unit_price and quantity are not provided.
    """

    quantity: int
    """Number of units for this line item."""

    unit_price: str
    """Price per unit in smallest currency unit."""


class LineItemsUpdateAddLineItemOperationTag(TypedDict, total=False):
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


class LineItemsUpdateAddLineItemOperation(TypedDict, total=False):
    """Operation to add a new line item to an invoice"""

    currency_code: Required[
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

    description: Required[str]
    """Description of the line item"""

    op: Required[Literal["add"]]
    """Operation type - add a new line item"""

    product_id: Required[str]
    """ID of the product/catalog item"""

    type: Required[Literal["payin", "payout"]]
    """The type of the line item"""

    user: Required[LineItemsUpdateAddLineItemOperationUser]
    """Identifies a user by Fragment-generated id or external_id (request body)."""

    amount: str
    """Deprecated: use price instead. Total amount in smallest currency unit."""

    price: LineItemsUpdateAddLineItemOperationPrice
    """Price breakdown. Provide amount, or unit_price + quantity, or all three."""

    tags: Iterable[LineItemsUpdateAddLineItemOperationTag]
    """Optional metadata tags for this line item"""


class LineItemsUpdateUpdateLineItemOperationPrice(TypedDict, total=False):
    """Price breakdown. Provide amount, or unit_price + quantity, or all three."""

    amount: str
    """Total amount in smallest currency unit.

    Required if unit_price and quantity are not provided.
    """

    quantity: int
    """Number of units for this line item."""

    unit_price: str
    """Price per unit in smallest currency unit."""


class LineItemsUpdateUpdateLineItemOperation(TypedDict, total=False):
    """Operation to update an existing line item pricing"""

    id: Required[str]
    """ID of the line item to update"""

    op: Required[Literal["update"]]
    """Operation type - update an existing line item"""

    amount: str
    """Deprecated: use price instead. Total amount in smallest currency unit."""

    price: LineItemsUpdateUpdateLineItemOperationPrice
    """Price breakdown. Provide amount, or unit_price + quantity, or all three."""


class LineItemsUpdateDeleteLineItemOperation(TypedDict, total=False):
    """Operation to delete a line item from an invoice"""

    id: Required[str]
    """ID of the line item to delete"""

    op: Required[Literal["delete"]]
    """Operation type - delete an existing line item"""


LineItemsUpdate: TypeAlias = Union[
    LineItemsUpdateAddLineItemOperation, LineItemsUpdateUpdateLineItemOperation, LineItemsUpdateDeleteLineItemOperation
]
