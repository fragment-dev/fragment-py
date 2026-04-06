# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import product_create_params
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
from ..types.product_list_response import ProductListResponse
from ..types.product_create_response import ProductCreateResponse
from ..types.product_retrieve_response import ProductRetrieveResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    """Product management operations"""

    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        description: str | Omit = omit,
        paid_by_roles: Iterable[product_create_params.PaidByRole] | Omit = omit,
        paid_to_roles: Iterable[product_create_params.PaidToRole] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCreateResponse:
        """
        Creates a new product.

        Args:
          code: Unique product code.

          description: Product description.

          paid_by_roles: Roles that can pay for the product. Reference roles by `id` or `name`. At least
              one of `paid_by_roles` or `paid_to_roles` must be provided.

          paid_to_roles: Roles that can receive payment for the product. Reference roles by `id` or
              `name`. At least one of `paid_by_roles` or `paid_to_roles` must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/products",
            body=maybe_transform(
                {
                    "code": code,
                    "description": description,
                    "paid_by_roles": paid_by_roles,
                    "paid_to_roles": paid_to_roles,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

    def retrieve(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveResponse:
        """Gets a product by code.

        Args:
          code: Product code.

        Must not include #, /, or :.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/products/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
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
    ) -> ProductListResponse:
        """Lists all products."""
        return self._get(
            "/products",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    """Product management operations"""

    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/fragment-dev/fragment-py#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/fragment-dev/fragment-py#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        description: str | Omit = omit,
        paid_by_roles: Iterable[product_create_params.PaidByRole] | Omit = omit,
        paid_to_roles: Iterable[product_create_params.PaidToRole] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductCreateResponse:
        """
        Creates a new product.

        Args:
          code: Unique product code.

          description: Product description.

          paid_by_roles: Roles that can pay for the product. Reference roles by `id` or `name`. At least
              one of `paid_by_roles` or `paid_to_roles` must be provided.

          paid_to_roles: Roles that can receive payment for the product. Reference roles by `id` or
              `name`. At least one of `paid_by_roles` or `paid_to_roles` must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/products",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "description": description,
                    "paid_by_roles": paid_by_roles,
                    "paid_to_roles": paid_to_roles,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

    async def retrieve(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveResponse:
        """Gets a product by code.

        Args:
          code: Product code.

        Must not include #, /, or :.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/products/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
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
    ) -> ProductListResponse:
        """Lists all products."""
        return await self._get(
            "/products",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
