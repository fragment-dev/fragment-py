# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    transaction_list_params,
    transaction_create_params,
    transaction_search_params,
    transaction_update_params,
    transaction_search_allocations_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.transaction_list_response import TransactionListResponse
from ..types.transaction_create_response import TransactionCreateResponse
from ..types.transaction_search_response import TransactionSearchResponse
from ..types.transaction_update_response import TransactionUpdateResponse
from ..types.transaction_retrieve_response import TransactionRetrieveResponse
from ..types.transaction_list_history_response import TransactionListHistoryResponse
from ..types.transaction_search_allocations_response import TransactionSearchAllocationsResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    """Transaction sync operations"""

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account: transaction_create_params.Account,
        allocations: Iterable[transaction_create_params.Allocation],
        amount: str,
        currency: Literal[
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
        ],
        external_id: str,
        posted: Union[str, datetime],
        tags: Iterable[transaction_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionCreateResponse:
        """
        Syncs a transaction, optionally with allocations

        Args:
          account: Account reference. Provide id, external_id, or both.

          allocations: Allocation entries for this transaction. Empty indicates unreconciled funds.

          amount: Amount in smallest currency unit as stringified bigint (can be positive or
              negative).

          currency: Currency code (ISO 4217 or crypto)

          external_id: External transaction ID used for idempotent sync.

          posted: Posted timestamp in ISO 8601 format.

          tags: Optional metadata tags for this transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transactions",
            body=maybe_transform(
                {
                    "account": account,
                    "allocations": allocations,
                    "amount": amount,
                    "currency": currency,
                    "external_id": external_id,
                    "posted": posted,
                    "tags": tags,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionCreateResponse,
        )

    def retrieve(
        self,
        transaction_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionRetrieveResponse:
        """
        Gets a transaction by ID or external ID

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return self._get(
            path_template("/transactions/{transaction_ref}", transaction_ref=transaction_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    def update(
        self,
        transaction_ref: str,
        *,
        current_transaction_version: int,
        allocations: transaction_update_params.Allocations | Omit = omit,
        tags: transaction_update_params.Tags | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionUpdateResponse:
        """
        Updates a transaction (tags, allocations, or both)

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          current_transaction_version: Current transaction version for optimistic concurrency control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return self._patch(
            path_template("/transactions/{transaction_ref}", transaction_ref=transaction_ref),
            body=maybe_transform(
                {
                    "current_transaction_version": current_transaction_version,
                    "allocations": allocations,
                    "tags": tags,
                },
                transaction_update_params.TransactionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionUpdateResponse,
        )

    def list(
        self,
        *,
        account: str | Omit = omit,
        reconciliation_status: Literal["reconciled", "unreconciled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListResponse:
        """Lists all transactions for the workspace

        Args:
          account: Filter by account.

        Encoded account ID (ext_account_xxx) or external_id. If the
              account does not exist, returns an empty list.

          reconciliation_status: Filter by reconciliation state. reconciled = unallocated_amount === 0;
              unreconciled = unallocated_amount !== 0. Omit for all transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "reconciliation_status": reconciliation_status,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )

    def list_history(
        self,
        transaction_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListHistoryResponse:
        """
        Gets the version history of a transaction

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return self._get(
            path_template("/transactions/{transaction_ref}/history", transaction_ref=transaction_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionListHistoryResponse,
        )

    def search(
        self,
        *,
        filter: transaction_search_params.Filter,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSearchResponse:
        """
        Searches transactions by filter criteria

        Args:
          filter: Filter criteria for searching transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transactions/search",
            body=maybe_transform({"filter": filter}, transaction_search_params.TransactionSearchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSearchResponse,
        )

    def search_allocations(
        self,
        *,
        filter: transaction_search_allocations_params.Filter,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSearchAllocationsResponse:
        """
        Searches transaction allocations by filter criteria

        Args:
          filter: Filter criteria for searching transaction allocations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transactions/allocations/search",
            body=maybe_transform(
                {"filter": filter}, transaction_search_allocations_params.TransactionSearchAllocationsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSearchAllocationsResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    """Transaction sync operations"""

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account: transaction_create_params.Account,
        allocations: Iterable[transaction_create_params.Allocation],
        amount: str,
        currency: Literal[
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
        ],
        external_id: str,
        posted: Union[str, datetime],
        tags: Iterable[transaction_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionCreateResponse:
        """
        Syncs a transaction, optionally with allocations

        Args:
          account: Account reference. Provide id, external_id, or both.

          allocations: Allocation entries for this transaction. Empty indicates unreconciled funds.

          amount: Amount in smallest currency unit as stringified bigint (can be positive or
              negative).

          currency: Currency code (ISO 4217 or crypto)

          external_id: External transaction ID used for idempotent sync.

          posted: Posted timestamp in ISO 8601 format.

          tags: Optional metadata tags for this transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transactions",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "allocations": allocations,
                    "amount": amount,
                    "currency": currency,
                    "external_id": external_id,
                    "posted": posted,
                    "tags": tags,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionCreateResponse,
        )

    async def retrieve(
        self,
        transaction_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionRetrieveResponse:
        """
        Gets a transaction by ID or external ID

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return await self._get(
            path_template("/transactions/{transaction_ref}", transaction_ref=transaction_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    async def update(
        self,
        transaction_ref: str,
        *,
        current_transaction_version: int,
        allocations: transaction_update_params.Allocations | Omit = omit,
        tags: transaction_update_params.Tags | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionUpdateResponse:
        """
        Updates a transaction (tags, allocations, or both)

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          current_transaction_version: Current transaction version for optimistic concurrency control.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return await self._patch(
            path_template("/transactions/{transaction_ref}", transaction_ref=transaction_ref),
            body=await async_maybe_transform(
                {
                    "current_transaction_version": current_transaction_version,
                    "allocations": allocations,
                    "tags": tags,
                },
                transaction_update_params.TransactionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionUpdateResponse,
        )

    async def list(
        self,
        *,
        account: str | Omit = omit,
        reconciliation_status: Literal["reconciled", "unreconciled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListResponse:
        """Lists all transactions for the workspace

        Args:
          account: Filter by account.

        Encoded account ID (ext_account_xxx) or external_id. If the
              account does not exist, returns an empty list.

          reconciliation_status: Filter by reconciliation state. reconciled = unallocated_amount === 0;
              unreconciled = unallocated_amount !== 0. Omit for all transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account": account,
                        "reconciliation_status": reconciliation_status,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=TransactionListResponse,
        )

    async def list_history(
        self,
        transaction_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionListHistoryResponse:
        """
        Gets the version history of a transaction

        Args:
          transaction_ref: Transaction reference. Accepts either an encoded Fragment ID (txn_xxx) or an
              external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_ref:
            raise ValueError(f"Expected a non-empty value for `transaction_ref` but received {transaction_ref!r}")
        return await self._get(
            path_template("/transactions/{transaction_ref}/history", transaction_ref=transaction_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionListHistoryResponse,
        )

    async def search(
        self,
        *,
        filter: transaction_search_params.Filter,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSearchResponse:
        """
        Searches transactions by filter criteria

        Args:
          filter: Filter criteria for searching transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transactions/search",
            body=await async_maybe_transform({"filter": filter}, transaction_search_params.TransactionSearchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSearchResponse,
        )

    async def search_allocations(
        self,
        *,
        filter: transaction_search_allocations_params.Filter,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSearchAllocationsResponse:
        """
        Searches transaction allocations by filter criteria

        Args:
          filter: Filter criteria for searching transaction allocations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transactions/allocations/search",
            body=await async_maybe_transform(
                {"filter": filter}, transaction_search_allocations_params.TransactionSearchAllocationsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSearchAllocationsResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            transactions.update,
        )
        self.list = to_raw_response_wrapper(
            transactions.list,
        )
        self.list_history = to_raw_response_wrapper(
            transactions.list_history,
        )
        self.search = to_raw_response_wrapper(
            transactions.search,
        )
        self.search_allocations = to_raw_response_wrapper(
            transactions.search_allocations,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_raw_response_wrapper(
            transactions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            transactions.update,
        )
        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )
        self.list_history = async_to_raw_response_wrapper(
            transactions.list_history,
        )
        self.search = async_to_raw_response_wrapper(
            transactions.search,
        )
        self.search_allocations = async_to_raw_response_wrapper(
            transactions.search_allocations,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.list_history = to_streamed_response_wrapper(
            transactions.list_history,
        )
        self.search = to_streamed_response_wrapper(
            transactions.search,
        )
        self.search_allocations = to_streamed_response_wrapper(
            transactions.search_allocations,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_streamed_response_wrapper(
            transactions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transactions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.list_history = async_to_streamed_response_wrapper(
            transactions.list_history,
        )
        self.search = async_to_streamed_response_wrapper(
            transactions.search,
        )
        self.search_allocations = async_to_streamed_response_wrapper(
            transactions.search_allocations,
        )
