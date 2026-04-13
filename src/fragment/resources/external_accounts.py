# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import external_account_create_params
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
from ..types.external_account_list_response import ExternalAccountListResponse
from ..types.external_account_create_response import ExternalAccountCreateResponse

__all__ = ["ExternalAccountsResource", "AsyncExternalAccountsResource"]


class ExternalAccountsResource(SyncAPIResource):
    """External account management operations"""

    @cached_property
    def with_raw_response(self) -> ExternalAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return ExternalAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return ExternalAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalAccountCreateResponse:
        """
        Creates an external account.

        Args:
          external_id: User-provided unique ID.

          name: Name of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external-accounts",
            body=maybe_transform(
                {
                    "external_id": external_id,
                    "name": name,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccountCreateResponse,
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
    ) -> ExternalAccountListResponse:
        """Lists all external accounts."""
        return self._get(
            "/external-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccountListResponse,
        )


class AsyncExternalAccountsResource(AsyncAPIResource):
    """External account management operations"""

    @cached_property
    def with_raw_response(self) -> AsyncExternalAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncExternalAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalAccountCreateResponse:
        """
        Creates an external account.

        Args:
          external_id: User-provided unique ID.

          name: Name of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external-accounts",
            body=await async_maybe_transform(
                {
                    "external_id": external_id,
                    "name": name,
                },
                external_account_create_params.ExternalAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccountCreateResponse,
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
    ) -> ExternalAccountListResponse:
        """Lists all external accounts."""
        return await self._get(
            "/external-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalAccountListResponse,
        )


class ExternalAccountsResourceWithRawResponse:
    def __init__(self, external_accounts: ExternalAccountsResource) -> None:
        self._external_accounts = external_accounts

        self.create = to_raw_response_wrapper(
            external_accounts.create,
        )
        self.list = to_raw_response_wrapper(
            external_accounts.list,
        )


class AsyncExternalAccountsResourceWithRawResponse:
    def __init__(self, external_accounts: AsyncExternalAccountsResource) -> None:
        self._external_accounts = external_accounts

        self.create = async_to_raw_response_wrapper(
            external_accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            external_accounts.list,
        )


class ExternalAccountsResourceWithStreamingResponse:
    def __init__(self, external_accounts: ExternalAccountsResource) -> None:
        self._external_accounts = external_accounts

        self.create = to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            external_accounts.list,
        )


class AsyncExternalAccountsResourceWithStreamingResponse:
    def __init__(self, external_accounts: AsyncExternalAccountsResource) -> None:
        self._external_accounts = external_accounts

        self.create = async_to_streamed_response_wrapper(
            external_accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            external_accounts.list,
        )
