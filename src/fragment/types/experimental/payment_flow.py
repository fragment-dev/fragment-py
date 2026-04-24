# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "PaymentFlow",
    "Invoice",
    "PaymentPlan",
    "PaymentPlanBatch",
    "PaymentPlanBatchPayment",
    "PaymentPlanBatchPaymentUser",
]


class Invoice(BaseModel):
    """Invoice being settled."""

    id: str
    """Invoice identifier."""

    external_id: Optional[str] = None
    """Invoice external ID."""


class PaymentPlanBatchPaymentUser(BaseModel):
    """User associated with the payment."""

    id: str
    """FRAGMENT generated unique ID."""

    external_id: str
    """User-provided unique ID."""


class PaymentPlanBatchPayment(BaseModel):
    amount: str
    """Amount in smallest currency unit."""

    currency: str
    """Currency code."""

    direction: str
    """Direction of the payment."""

    payment_id: str
    """FRAGMENT generated unique ID."""

    status: str
    """Status of the payment."""

    user: PaymentPlanBatchPaymentUser
    """User associated with the payment."""


class PaymentPlanBatch(BaseModel):
    batch_id: str
    """Batch identifier."""

    depends_on: List[str]
    """Batches this one depends on."""

    label: str
    """Human-readable batch label."""

    payments: List[PaymentPlanBatchPayment]
    """Payments in this batch."""

    status: str
    """Batch status."""


class PaymentPlan(BaseModel):
    """Payment plan for UI rendering."""

    batches: List[PaymentPlanBatch]
    """Payment batches."""

    generated_at: str
    """When the plan was generated."""

    invoice_id: str
    """Invoice identifier."""

    version: float
    """Plan version."""


class PaymentFlow(BaseModel):
    """Payment flow object."""

    id: str
    """FRAGMENT generated unique ID."""

    created: str
    """Timestamp when the payment flow was created."""

    external_id: str
    """User-provided unique external ID."""

    invoice: Invoice
    """Invoice being settled."""

    modified: str
    """Timestamp when the payment flow was last modified."""

    payment_plan: PaymentPlan
    """Payment plan for UI rendering."""

    status: str
    """Status of the payment flow."""

    type: str
    """Type of payment flow."""
