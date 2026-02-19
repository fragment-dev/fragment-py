# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "InvoiceRetrieveResponse",
    "Data",
    "DataBalance",
    "DataBalanceNet",
    "DataBalancePayins",
    "DataBalancePayouts",
    "DataUser",
    "DataUserBalance",
    "DataUserBalanceNet",
    "DataUserBalancePayins",
    "DataUserBalancePayouts",
    "DataLineItem",
]


class DataBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataBalanceNet

    payins: DataBalancePayins

    payouts: DataBalancePayouts


class DataUserBalanceNet(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalancePayins(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalancePayouts(BaseModel):
    actual: str
    """Actual amount (represented as string)"""

    expected: str
    """Expected amount (represented as string)"""

    remaining: str
    """Remaining amount (expected - actual, represented as string)"""


class DataUserBalance(BaseModel):
    currency: str
    """Currency code"""

    net: DataUserBalanceNet

    payins: DataUserBalancePayins

    payouts: DataUserBalancePayouts


class DataUser(BaseModel):
    id: str
    """User/party ID"""

    balances: List[DataUserBalance]
    """Per-currency balance breakdown for this user"""


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
    ] = FieldInfo(alias="currencyCode")
    """Currency code (ISO 4217 or crypto)"""

    description: str
    """Description of the line item"""

    product_id: str
    """ID of the product/catalog item"""

    type: Literal["payin", "payout"]
    """The type of the line item"""

    user_id: str
    """External ID of the user associated with this line item"""


class Data(BaseModel):
    """Invoice with balance details"""

    id: str
    """Unique identifier for the invoice"""

    balances: List[DataBalance]
    """Invoice-level balances by currency: payins, payouts, and net (payins - payouts)"""

    created: datetime
    """ISO 8601 timestamp when the invoice was created"""

    status: Literal["active"]
    """The status of the invoice"""

    users: List[DataUser]
    """Users/parties involved in the invoice"""

    version: float
    """The current version of the invoice.

    Pass this value when updating to ensure thread safety.
    """

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID this invoice belongs to"""

    line_items: Optional[List[DataLineItem]] = FieldInfo(alias="lineItems", default=None)
    """List of line items associated with this invoice"""

    modified: Optional[datetime] = None
    """ISO 8601 timestamp when the invoice was last modified"""


class InvoiceRetrieveResponse(BaseModel):
    data: Data
    """Invoice with balance details"""
