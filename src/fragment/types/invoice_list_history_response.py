# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .invoice import Invoice
from .._models import BaseModel

__all__ = [
    "InvoiceListHistoryResponse",
    "Data",
    "DataDiff",
    "DataDiffAddDiffEntry",
    "DataDiffAddDiffEntryItem",
    "DataDiffAddDiffEntryItemPrice",
    "DataDiffAddDiffEntryItemTag",
    "DataDiffUpdateDiffEntry",
    "DataDiffUpdateDiffEntryNewPrice",
    "DataDiffUpdateDiffEntryOldPrice",
    "DataDiffDeleteDiffEntry",
    "DataDiffDeleteDiffEntryItem",
    "DataDiffDeleteDiffEntryItemPrice",
    "DataDiffDeleteDiffEntryItemTag",
]


class DataDiffAddDiffEntryItemPrice(BaseModel):
    """Price breakdown containing amount, unit price, and quantity"""

    amount: str
    """Total amount in smallest currency unit (represented as string for bigint)"""

    quantity: int
    """Quantity of units for this line item"""

    unit_price: str
    """Unit price in smallest currency unit (represented as string for bigint)"""


class DataDiffAddDiffEntryItemTag(BaseModel):
    """A key-value tag pair"""

    key: str
    """Tag key"""

    value: str
    """Tag value"""


class DataDiffAddDiffEntryItem(BaseModel):
    """Invoice line item object"""

    id: str
    """Unique identifier for the line item"""

    amount: str
    """Deprecated: use price.amount instead.

    Total amount in smallest currency unit (represented as string for bigint)
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
    """Currency code (ISO 4217 or crypto)"""

    description: str
    """Description of the line item"""

    price: DataDiffAddDiffEntryItemPrice
    """Price breakdown containing amount, unit price, and quantity"""

    product_id: str
    """ID of the product/catalog item"""

    tags: List[DataDiffAddDiffEntryItemTag]
    """Metadata tags for this line item"""

    type: Literal["payin", "payout"]
    """The type of the line item"""

    user_id: str
    """External ID of the user associated with this line item"""


class DataDiffAddDiffEntry(BaseModel):
    item: DataDiffAddDiffEntryItem
    """Invoice line item object"""

    op: Literal["add"]
    """A line item was added"""


class DataDiffUpdateDiffEntryNewPrice(BaseModel):
    """Price breakdown containing amount, unit price, and quantity"""

    amount: str
    """Total amount in smallest currency unit (represented as string for bigint)"""

    quantity: int
    """Quantity of units for this line item"""

    unit_price: str
    """Unit price in smallest currency unit (represented as string for bigint)"""


class DataDiffUpdateDiffEntryOldPrice(BaseModel):
    """Price breakdown containing amount, unit price, and quantity"""

    amount: str
    """Total amount in smallest currency unit (represented as string for bigint)"""

    quantity: int
    """Quantity of units for this line item"""

    unit_price: str
    """Unit price in smallest currency unit (represented as string for bigint)"""


class DataDiffUpdateDiffEntry(BaseModel):
    id: str
    """ID of the updated line item"""

    new_amount: str
    """Deprecated: use new_price.amount instead. New amount after the update"""

    new_price: DataDiffUpdateDiffEntryNewPrice
    """Price breakdown containing amount, unit price, and quantity"""

    old_amount: str
    """Deprecated: use old_price.amount instead. Amount before the update"""

    old_price: DataDiffUpdateDiffEntryOldPrice
    """Price breakdown containing amount, unit price, and quantity"""

    op: Literal["update"]
    """A line item was updated"""


class DataDiffDeleteDiffEntryItemPrice(BaseModel):
    """Price breakdown containing amount, unit price, and quantity"""

    amount: str
    """Total amount in smallest currency unit (represented as string for bigint)"""

    quantity: int
    """Quantity of units for this line item"""

    unit_price: str
    """Unit price in smallest currency unit (represented as string for bigint)"""


class DataDiffDeleteDiffEntryItemTag(BaseModel):
    """A key-value tag pair"""

    key: str
    """Tag key"""

    value: str
    """Tag value"""


class DataDiffDeleteDiffEntryItem(BaseModel):
    """Invoice line item object"""

    id: str
    """Unique identifier for the line item"""

    amount: str
    """Deprecated: use price.amount instead.

    Total amount in smallest currency unit (represented as string for bigint)
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
    """Currency code (ISO 4217 or crypto)"""

    description: str
    """Description of the line item"""

    price: DataDiffDeleteDiffEntryItemPrice
    """Price breakdown containing amount, unit price, and quantity"""

    product_id: str
    """ID of the product/catalog item"""

    tags: List[DataDiffDeleteDiffEntryItemTag]
    """Metadata tags for this line item"""

    type: Literal["payin", "payout"]
    """The type of the line item"""

    user_id: str
    """External ID of the user associated with this line item"""


class DataDiffDeleteDiffEntry(BaseModel):
    item: DataDiffDeleteDiffEntryItem
    """Invoice line item object"""

    op: Literal["delete"]
    """A line item was deleted"""


DataDiff: TypeAlias = Union[DataDiffAddDiffEntry, DataDiffUpdateDiffEntry, DataDiffDeleteDiffEntry]


class Data(Invoice):
    """A versioned snapshot of an invoice"""

    diff: Optional[List[DataDiff]] = None
    """Cumulative diff of changes applied to the invoice"""

    version: Optional[float] = None  # type: ignore
    """Version number of this invoice snapshot"""


class InvoiceListHistoryResponse(BaseModel):
    """Version history of an invoice"""

    data: List[Data]
