# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._oauth2 import OAuth2ClientCredentials, make_oauth2
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import roles, users, invoices, platform, products
    from .resources.roles import RolesResource, AsyncRolesResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.platform import PlatformResource, AsyncPlatformResource
    from .resources.products import ProductsResource, AsyncProductsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Fragment",
    "AsyncFragment",
    "Client",
    "AsyncClient",
]


class Fragment(SyncAPIClient):
    # client options
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Fragment client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `FRAGMENT_CLIENT_ID`
        - `client_secret` from `FRAGMENT_CLIENT_SECRET`
        """
        if client_id is None:
            client_id = os.environ.get("FRAGMENT_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FRAGMENT_CLIENT_SECRET")
        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("FRAGMENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.us-west-2.fragment.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def invoices(self) -> InvoicesResource:
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def platform(self) -> PlatformResource:
        from .resources.platform import PlatformResource

        return PlatformResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def roles(self) -> RolesResource:
        from .resources.roles import RolesResource

        return RolesResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def with_raw_response(self) -> FragmentWithRawResponse:
        return FragmentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FragmentWithStreamedResponse:
        return FragmentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        if self.client_id and self.client_secret:
            return make_oauth2(
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_url=self._prepare_url("https://auth.us-west-2.fragment.dev/oauth2/token"),
                header="Authorization",
            )
        return None

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFragment(AsyncAPIClient):
    # client options
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncFragment client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `FRAGMENT_CLIENT_ID`
        - `client_secret` from `FRAGMENT_CLIENT_SECRET`
        """
        if client_id is None:
            client_id = os.environ.get("FRAGMENT_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FRAGMENT_CLIENT_SECRET")
        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("FRAGMENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.us-west-2.fragment.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def platform(self) -> AsyncPlatformResource:
        from .resources.platform import AsyncPlatformResource

        return AsyncPlatformResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        from .resources.roles import AsyncRolesResource

        return AsyncRolesResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncFragmentWithRawResponse:
        return AsyncFragmentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFragmentWithStreamedResponse:
        return AsyncFragmentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        if self.client_id and self.client_secret:
            return make_oauth2(
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_url=self._prepare_url("https://auth.us-west-2.fragment.dev/oauth2/token"),
                header="Authorization",
            )
        return None

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FragmentWithRawResponse:
    _client: Fragment

    def __init__(self, client: Fragment) -> None:
        self._client = client

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def platform(self) -> platform.PlatformResourceWithRawResponse:
        from .resources.platform import PlatformResourceWithRawResponse

        return PlatformResourceWithRawResponse(self._client.platform)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def roles(self) -> roles.RolesResourceWithRawResponse:
        from .resources.roles import RolesResourceWithRawResponse

        return RolesResourceWithRawResponse(self._client.roles)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)


class AsyncFragmentWithRawResponse:
    _client: AsyncFragment

    def __init__(self, client: AsyncFragment) -> None:
        self._client = client

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def platform(self) -> platform.AsyncPlatformResourceWithRawResponse:
        from .resources.platform import AsyncPlatformResourceWithRawResponse

        return AsyncPlatformResourceWithRawResponse(self._client.platform)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithRawResponse:
        from .resources.roles import AsyncRolesResourceWithRawResponse

        return AsyncRolesResourceWithRawResponse(self._client.roles)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)


class FragmentWithStreamedResponse:
    _client: Fragment

    def __init__(self, client: Fragment) -> None:
        self._client = client

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def platform(self) -> platform.PlatformResourceWithStreamingResponse:
        from .resources.platform import PlatformResourceWithStreamingResponse

        return PlatformResourceWithStreamingResponse(self._client.platform)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def roles(self) -> roles.RolesResourceWithStreamingResponse:
        from .resources.roles import RolesResourceWithStreamingResponse

        return RolesResourceWithStreamingResponse(self._client.roles)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)


class AsyncFragmentWithStreamedResponse:
    _client: AsyncFragment

    def __init__(self, client: AsyncFragment) -> None:
        self._client = client

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def platform(self) -> platform.AsyncPlatformResourceWithStreamingResponse:
        from .resources.platform import AsyncPlatformResourceWithStreamingResponse

        return AsyncPlatformResourceWithStreamingResponse(self._client.platform)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def roles(self) -> roles.AsyncRolesResourceWithStreamingResponse:
        from .resources.roles import AsyncRolesResourceWithStreamingResponse

        return AsyncRolesResourceWithStreamingResponse(self._client.roles)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Fragment

AsyncClient = AsyncFragment
