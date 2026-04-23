# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["PaymentFlowCreateParams", "Invoice", "InvoiceID", "InvoiceExternalID"]


class PaymentFlowCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """User-provided unique external ID."""

    invoice: Required[Invoice]
    """Invoice to settle."""

    type: Required[Literal["single_invoice_settlement"]]
    """Type of payment flow."""


class InvoiceID(TypedDict, total=False):
    id: Required[str]
    """Fragment invoice ID."""


class InvoiceExternalID(TypedDict, total=False):
    external_id: Required[str]
    """Invoice external ID."""


Invoice: TypeAlias = Union[InvoiceID, InvoiceExternalID]
