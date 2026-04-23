# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .payment_flows import (
    PaymentFlowsResource,
    AsyncPaymentFlowsResource,
    PaymentFlowsResourceWithRawResponse,
    AsyncPaymentFlowsResourceWithRawResponse,
    PaymentFlowsResourceWithStreamingResponse,
    AsyncPaymentFlowsResourceWithStreamingResponse,
)

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def payment_flows(self) -> PaymentFlowsResource:
        """Payment flow operations"""
        return PaymentFlowsResource(self._client)

    @cached_property
    def payments(self) -> PaymentsResource:
        """Payment operations"""
        return PaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return ExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return ExperimentalResourceWithStreamingResponse(self)


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def payment_flows(self) -> AsyncPaymentFlowsResource:
        """Payment flow operations"""
        return AsyncPaymentFlowsResource(self._client)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        """Payment operations"""
        return AsyncPaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncExperimentalResourceWithStreamingResponse(self)


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def payment_flows(self) -> PaymentFlowsResourceWithRawResponse:
        """Payment flow operations"""
        return PaymentFlowsResourceWithRawResponse(self._experimental.payment_flows)

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        """Payment operations"""
        return PaymentsResourceWithRawResponse(self._experimental.payments)


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def payment_flows(self) -> AsyncPaymentFlowsResourceWithRawResponse:
        """Payment flow operations"""
        return AsyncPaymentFlowsResourceWithRawResponse(self._experimental.payment_flows)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        """Payment operations"""
        return AsyncPaymentsResourceWithRawResponse(self._experimental.payments)


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def payment_flows(self) -> PaymentFlowsResourceWithStreamingResponse:
        """Payment flow operations"""
        return PaymentFlowsResourceWithStreamingResponse(self._experimental.payment_flows)

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        """Payment operations"""
        return PaymentsResourceWithStreamingResponse(self._experimental.payments)


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def payment_flows(self) -> AsyncPaymentFlowsResourceWithStreamingResponse:
        """Payment flow operations"""
        return AsyncPaymentFlowsResourceWithStreamingResponse(self._experimental.payment_flows)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """Payment operations"""
        return AsyncPaymentsResourceWithStreamingResponse(self._experimental.payments)
