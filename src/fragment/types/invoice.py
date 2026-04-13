# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Invoice", "Tag", "LineItem", "LineItemPrice", "LineItemTag"]


class Tag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class LineItemPrice(BaseModel):
    """Price breakdown."""

    amount: str
    """Total amount as a string in the smallest currency unit, such as cents for USD."""

    quantity: int
    """Number of units."""

    unit_price: str
    """Unit price as a string in the smallest currency unit, such as cents for USD."""


class LineItemTag(BaseModel):
    """A key-value tag pair."""

    key: str
    """Tag key."""

    value: str
    """Tag value."""


class LineItem(BaseModel):
    """Invoice line item."""

    id: str
    """FRAGMENT generated unique ID."""

    amount: str
    """Total amount as a string in the smallest currency unit, such as cents for USD.

    Deprecated, use price.amount instead.
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

    description: str
    """Description of the line item."""

    price: LineItemPrice
    """Price breakdown."""

    product_id: str
    """Unique identifier for the product."""

    tags: List[LineItemTag]
    """Tags for the line item."""

    type: Literal["payin", "payout"]
    """Type of the line item."""

    user_id: str
    """User-provided unique external ID."""


class Invoice(BaseModel):
    """Invoice object."""

    id: str
    """Unique invoice ID."""

    created: datetime
    """Timestamp when the invoice was created. Uses ISO 8601 format."""

    status: Literal["active"]
    """Status of the invoice. Deprecated."""

    tags: List[Tag]
    """Tags for the invoice."""

    version: float
    """Current version of the invoice."""

    workspace_id: str
    """Workspace the invoice belongs to."""

    line_items: Optional[List[LineItem]] = None
    """Line items for the invoice."""

    modified: Optional[datetime] = None
    """Timestamp when the invoice was last modified. Uses ISO 8601 format."""
