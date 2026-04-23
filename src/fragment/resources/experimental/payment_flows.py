# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.experimental import payment_flow_create_params, payment_flow_search_params
from ...types.experimental.payment_flow_create_response import PaymentFlowCreateResponse
from ...types.experimental.payment_flow_search_response import PaymentFlowSearchResponse
from ...types.experimental.payment_flow_retrieve_response import PaymentFlowRetrieveResponse

__all__ = ["PaymentFlowsResource", "AsyncPaymentFlowsResource"]


class PaymentFlowsResource(SyncAPIResource):
    """Payment flow operations"""

    @cached_property
    def with_raw_response(self) -> PaymentFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return PaymentFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return PaymentFlowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        invoice: payment_flow_create_params.Invoice,
        type: Literal["single_invoice_settlement"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowCreateResponse:
        """
        Creates a new payment flow.

        Args:
          external_id: User-provided unique external ID.

          invoice: Invoice to settle.

          type: Type of payment flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payment-flows",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "invoice": invoice,
                    "type": type,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowCreateResponse,
        )

    def retrieve(
        self,
        payment_flow_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowRetrieveResponse:
        """
        Gets a payment flow by ID or external ID.

        Args:
          payment_flow_ref: Payment flow ID or external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_flow_ref:
            raise ValueError(f"Expected a non-empty value for `payment_flow_ref` but received {payment_flow_ref!r}")
        return self._get(
            path_template("/payment-flows/{payment_flow_ref}", payment_flow_ref=payment_flow_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowRetrieveResponse,
        )

    def search(
        self,
        *,
        invoice_id: str | Omit = omit,
        page_info: payment_flow_search_params.PageInfo | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowSearchResponse:
        """
        Searches payment flows.

        Args:
          invoice_id: Filter by invoice ID.

          page_info: Pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payment-flows/search",
            body=maybe_transform(
                {
                    "invoice_id": invoice_id,
                    "page_info": page_info,
                },
                payment_flow_search_params.PaymentFlowSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowSearchResponse,
        )


class AsyncPaymentFlowsResource(AsyncAPIResource):
    """Payment flow operations"""

    @cached_property
    def with_raw_response(self) -> AsyncPaymentFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncPaymentFlowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        invoice: payment_flow_create_params.Invoice,
        type: Literal["single_invoice_settlement"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowCreateResponse:
        """
        Creates a new payment flow.

        Args:
          external_id: User-provided unique external ID.

          invoice: Invoice to settle.

          type: Type of payment flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payment-flows",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "invoice": invoice,
                    "type": type,
                },
                payment_flow_create_params.PaymentFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowCreateResponse,
        )

    async def retrieve(
        self,
        payment_flow_ref: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowRetrieveResponse:
        """
        Gets a payment flow by ID or external ID.

        Args:
          payment_flow_ref: Payment flow ID or external ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_flow_ref:
            raise ValueError(f"Expected a non-empty value for `payment_flow_ref` but received {payment_flow_ref!r}")
        return await self._get(
            path_template("/payment-flows/{payment_flow_ref}", payment_flow_ref=payment_flow_ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowRetrieveResponse,
        )

    async def search(
        self,
        *,
        invoice_id: str | Omit = omit,
        page_info: payment_flow_search_params.PageInfo | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentFlowSearchResponse:
        """
        Searches payment flows.

        Args:
          invoice_id: Filter by invoice ID.

          page_info: Pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payment-flows/search",
            body=await async_maybe_transform(
                {
                    "invoice_id": invoice_id,
                    "page_info": page_info,
                },
                payment_flow_search_params.PaymentFlowSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentFlowSearchResponse,
        )


class PaymentFlowsResourceWithRawResponse:
    def __init__(self, payment_flows: PaymentFlowsResource) -> None:
        self._payment_flows = payment_flows

        self.create = to_raw_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_flows.retrieve,
        )
        self.search = to_raw_response_wrapper(
            payment_flows.search,
        )


class AsyncPaymentFlowsResourceWithRawResponse:
    def __init__(self, payment_flows: AsyncPaymentFlowsResource) -> None:
        self._payment_flows = payment_flows

        self.create = async_to_raw_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_flows.retrieve,
        )
        self.search = async_to_raw_response_wrapper(
            payment_flows.search,
        )


class PaymentFlowsResourceWithStreamingResponse:
    def __init__(self, payment_flows: PaymentFlowsResource) -> None:
        self._payment_flows = payment_flows

        self.create = to_streamed_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_flows.retrieve,
        )
        self.search = to_streamed_response_wrapper(
            payment_flows.search,
        )


class AsyncPaymentFlowsResourceWithStreamingResponse:
    def __init__(self, payment_flows: AsyncPaymentFlowsResource) -> None:
        self._payment_flows = payment_flows

        self.create = async_to_streamed_response_wrapper(
            payment_flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_flows.retrieve,
        )
        self.search = async_to_streamed_response_wrapper(
            payment_flows.search,
        )
