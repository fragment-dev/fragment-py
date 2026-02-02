# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InvoiceUpdateParams",
    "LineItemsUpdate",
    "LineItemsUpdateAddLineItemOperation",
    "LineItemsUpdateAddLineItemOperationPayoutUser",
    "LineItemsUpdateAddLineItemOperationPayoutUserPlatformPayoutInput",
    "LineItemsUpdateAddLineItemOperationPayoutUserUserPayoutInput",
    "LineItemsUpdateUpdateLineItemOperation",
    "LineItemsUpdateDeleteLineItemOperation",
]


class InvoiceUpdateParams(TypedDict, total=False):
    line_items_update: Required[Iterable[LineItemsUpdate]]
    """List of line item operations to apply to the invoice"""


class LineItemsUpdateAddLineItemOperationPayoutUserPlatformPayoutInput(TypedDict, total=False):
    platform: Required[Literal[True]]
    """Set to true for platform payout"""


class LineItemsUpdateAddLineItemOperationPayoutUserUserPayoutInput(TypedDict, total=False):
    user_id: Required[str]
    """External ID of the user receiving payout"""

    platform: Literal[False]
    """Set to false or omit for user payout"""


LineItemsUpdateAddLineItemOperationPayoutUser: TypeAlias = Union[
    LineItemsUpdateAddLineItemOperationPayoutUserPlatformPayoutInput,
    LineItemsUpdateAddLineItemOperationPayoutUserUserPayoutInput,
]


class LineItemsUpdateAddLineItemOperation(TypedDict, total=False):
    """Operation to add a new line item to an invoice"""

    amount: Required[str]
    """Amount in smallest currency unit (e.g., cents)"""

    currency_code: Required[
        Literal[
            "ADA",
            "BTC",
            "DAI",
            "ETH",
            "SOL",
            "USDC",
            "USDT",
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

    payout_user: Required[LineItemsUpdateAddLineItemOperationPayoutUser]
    """The user receiving payout - either platform or a user"""

    product_id: Required[str]
    """ID of the product/catalog item"""


class LineItemsUpdateUpdateLineItemOperation(TypedDict, total=False):
    """Operation to update an existing line item amount"""

    id: Required[str]
    """ID of the line item to update"""

    amount: Required[str]
    """New amount in smallest currency unit"""

    op: Required[Literal["update"]]
    """Operation type - update an existing line item"""


class LineItemsUpdateDeleteLineItemOperation(TypedDict, total=False):
    """Operation to delete a line item from an invoice"""

    id: Required[str]
    """ID of the line item to delete"""

    op: Required[Literal["delete"]]
    """Operation type - delete an existing line item"""


LineItemsUpdate: TypeAlias = Union[
    LineItemsUpdateAddLineItemOperation, LineItemsUpdateUpdateLineItemOperation, LineItemsUpdateDeleteLineItemOperation
]
