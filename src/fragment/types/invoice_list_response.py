# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "InvoiceListResponse",
    "Data",
    "DataLineItem",
    "DataLineItemPayoutParty",
    "DataLineItemPayoutPartyPlatformPayoutResponse",
    "DataLineItemPayoutPartyCounterPartyPayoutResponse",
]


class DataLineItemPayoutPartyPlatformPayoutResponse(BaseModel):
    platform: Literal[True]
    """Set to true for platform payout"""


class DataLineItemPayoutPartyCounterPartyPayoutResponse(BaseModel):
    party_id: str
    """External ID of the party receiving payout"""

    platform: Optional[Literal[False]] = None
    """Set to false or omit for counter-party payout"""


DataLineItemPayoutParty: TypeAlias = Union[
    DataLineItemPayoutPartyPlatformPayoutResponse, DataLineItemPayoutPartyCounterPartyPayoutResponse
]


class DataLineItem(BaseModel):
    """Invoice line item object"""

    id: str
    """Unique identifier for the line item"""

    amount: str
    """Amount in smallest currency unit (represented as string for bigint)"""

    currency_code: Literal[
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
    ] = FieldInfo(alias="currencyCode")
    """Currency code (ISO 4217 or crypto)"""

    description: str
    """Description of the line item"""

    payout_party: DataLineItemPayoutParty
    """The party receiving payout - either platform or a counter-party"""

    product_id: str
    """ID of the product/catalog item"""


class Data(BaseModel):
    """Invoice object"""

    id: str
    """Unique identifier for the invoice"""

    buyer_party: str = FieldInfo(alias="buyerParty")
    """External ID of the buyer party"""

    created: datetime
    """ISO 8601 timestamp when the invoice was created"""

    status: Literal["draft", "active", "closed", "void", "failed"]
    """The status of the invoice"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this invoice belongs to"""

    line_items: Optional[List[DataLineItem]] = FieldInfo(alias="lineItems", default=None)
    """List of line items associated with this invoice"""

    modified: Optional[datetime] = None
    """ISO 8601 timestamp when the invoice was last modified"""


class InvoiceListResponse(BaseModel):
    """List of invoices"""

    data: List[Data]
