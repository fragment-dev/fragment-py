# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import platform_update_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.platform_update_response import PlatformUpdateResponse
from ..types.platform_retrieve_response import PlatformRetrieveResponse

__all__ = ["PlatformResource", "AsyncPlatformResource"]


class PlatformResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return PlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return PlatformResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformRetrieveResponse:
        """Gets platform details for the workspace"""
        return self._get(
            "/platform",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformRetrieveResponse,
        )

    def update(
        self,
        *,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformUpdateResponse:
        """
        Updates platform details (creates if not exists)

        Args:
          display_name: Display name for the platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/platform",
            body=maybe_transform({"display_name": display_name}, platform_update_params.PlatformUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformUpdateResponse,
        )


class AsyncPlatformResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncPlatformResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformRetrieveResponse:
        """Gets platform details for the workspace"""
        return await self._get(
            "/platform",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformRetrieveResponse,
        )

    async def update(
        self,
        *,
        display_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformUpdateResponse:
        """
        Updates platform details (creates if not exists)

        Args:
          display_name: Display name for the platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/platform",
            body=await async_maybe_transform(
                {"display_name": display_name}, platform_update_params.PlatformUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformUpdateResponse,
        )


class PlatformResourceWithRawResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

        self.retrieve = to_raw_response_wrapper(
            platform.retrieve,
        )
        self.update = to_raw_response_wrapper(
            platform.update,
        )


class AsyncPlatformResourceWithRawResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

        self.retrieve = async_to_raw_response_wrapper(
            platform.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            platform.update,
        )


class PlatformResourceWithStreamingResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

        self.retrieve = to_streamed_response_wrapper(
            platform.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            platform.update,
        )


class AsyncPlatformResourceWithStreamingResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

        self.retrieve = async_to_streamed_response_wrapper(
            platform.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            platform.update,
        )
