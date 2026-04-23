# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Payment"]


class Payment(BaseModel):
    """Payment object."""

    id: str
    """FRAGMENT generated unique ID."""

    amount: str
    """Amount in smallest currency unit."""

    created: str
    """Timestamp when the payment was created."""

    currency: str
    """Currency code."""

    direction: str
    """Direction of the payment."""

    modified: str
    """Timestamp when the payment was last modified."""

    payment_account_id: str
    """Payment account ID."""

    payment_flow_id: str
    """Payment flow ID."""

    status: str
    """Status of the payment."""

    transaction_ids: List[str]
    """Associated transaction IDs."""

    external_id: Optional[str] = None
    """User-provided unique ID when the payment was created with one."""
