# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    account: str
    """Filter by account.

    Encoded account ID (ext_account_xxx) or external_id. If the account does not
    exist, returns an empty list.
    """

    reconciliation_status: Literal["reconciled", "unreconciled"]
    """Filter by reconciliation state.

    reconciled = unallocated_amount === 0; unreconciled = unallocated_amount !== 0.
    Omit for all transactions.
    """
