# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "InvoiceCreateParams",
    "LineItem",
    "LineItemPayoutParty",
    "LineItemPayoutPartyPlatformPayout",
    "LineItemPayoutPartyCounterPartyPayout",
]


class InvoiceCreateParams(TypedDict, total=False):
    buyer_party: Required[Annotated[str, PropertyInfo(alias="buyerParty")]]
    """External ID of the buyer party"""

    invoice_id: Required[Annotated[str, PropertyInfo(alias="invoiceId")]]
    """Unique identifier for the invoice.

    Make this the canonical ID from your system for the transaction.
    """

    line_items: Annotated[Iterable[LineItem], PropertyInfo(alias="lineItems")]
    """Optional list of line items to create with the invoice"""

    status: Literal["draft", "active"]
    """Initial status of the invoice. Defaults to active if not specified."""


class LineItemPayoutPartyPlatformPayout(TypedDict, total=False):
    platform: Required[Literal[True]]
    """Set to true for platform payout"""


class LineItemPayoutPartyCounterPartyPayout(TypedDict, total=False):
    party_id: Required[str]
    """External ID of the party receiving payout"""

    platform: Literal[False]
    """Set to false or omit for counter-party payout"""


LineItemPayoutParty: TypeAlias = Union[LineItemPayoutPartyPlatformPayout, LineItemPayoutPartyCounterPartyPayout]


class LineItem(TypedDict, total=False):
    """Line item data for creating within an invoice.

    The payInParty is automatically set to the invoice's buyerParty.
    """

    amount: Required[str]
    """Amount in smallest currency unit (e.g., cents)"""

    currency_code: Required[
        Annotated[
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
            ],
            PropertyInfo(alias="currencyCode"),
        ]
    ]
    """Currency code (ISO 4217 or crypto)"""

    description: Required[str]
    """Description of the line item"""

    payout_party: Required[LineItemPayoutParty]
    """The party receiving payout - either platform or a counter-party"""

    product_id: Required[str]
    """ID of the product/catalog item"""
