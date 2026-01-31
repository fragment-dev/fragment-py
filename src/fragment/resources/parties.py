# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import party_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.party_list_response import PartyListResponse
from ..types.party_create_response import PartyCreateResponse
from ..types.party_retrieve_response import PartyRetrieveResponse

__all__ = ["PartiesResource", "AsyncPartiesResource"]


class PartiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return PartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return PartiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyCreateResponse:
        """
        Creates a new party

        Args:
          external_id: External ID for the party

          type: Type of the counterparty (e.g., buyer, seller)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parties",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "type": type,
                },
                party_create_params.PartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyCreateResponse,
        )

    def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyRetrieveResponse:
        """
        Gets a party by external ID

        Args:
          external_id: External ID of the party

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/parties/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyListResponse:
        """Lists all parties for the workspace"""
        return self._get(
            "/parties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyListResponse,
        )


class AsyncPartiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPartiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncPartiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyCreateResponse:
        """
        Creates a new party

        Args:
          external_id: External ID for the party

          type: Type of the counterparty (e.g., buyer, seller)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parties",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "type": type,
                },
                party_create_params.PartyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyCreateResponse,
        )

    async def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyRetrieveResponse:
        """
        Gets a party by external ID

        Args:
          external_id: External ID of the party

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/parties/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartyListResponse:
        """Lists all parties for the workspace"""
        return await self._get(
            "/parties",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartyListResponse,
        )


class PartiesResourceWithRawResponse:
    def __init__(self, parties: PartiesResource) -> None:
        self._parties = parties

        self.create = to_raw_response_wrapper(
            parties.create,
        )
        self.retrieve = to_raw_response_wrapper(
            parties.retrieve,
        )
        self.list = to_raw_response_wrapper(
            parties.list,
        )


class AsyncPartiesResourceWithRawResponse:
    def __init__(self, parties: AsyncPartiesResource) -> None:
        self._parties = parties

        self.create = async_to_raw_response_wrapper(
            parties.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            parties.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            parties.list,
        )


class PartiesResourceWithStreamingResponse:
    def __init__(self, parties: PartiesResource) -> None:
        self._parties = parties

        self.create = to_streamed_response_wrapper(
            parties.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            parties.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            parties.list,
        )


class AsyncPartiesResourceWithStreamingResponse:
    def __init__(self, parties: AsyncPartiesResource) -> None:
        self._parties = parties

        self.create = async_to_streamed_response_wrapper(
            parties.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            parties.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            parties.list,
        )
