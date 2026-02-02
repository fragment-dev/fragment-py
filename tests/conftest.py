# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import httpx
import pytest
from pytest_asyncio import is_async_test

from fragment import Fragment, AsyncFragment, DefaultAioHttpClient
from fragment._utils import is_dict

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest  # pyright: ignore[reportPrivateImportUsage]

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("fragment").setLevel(logging.DEBUG)

def _clear_oauth2_cache() -> None:
    from fragment._oauth2 import make_oauth2

    cache_clear = getattr(make_oauth2, "cache_clear", None)
    if callable(cache_clear):
        cache_clear()


# automatically add `pytest.mark.asyncio()` to all of our async tests
# so we don't have to add that boilerplate everywhere
def pytest_collection_modifyitems(items: list[pytest.Function]) -> None:
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)

    # We skip tests that use both the aiohttp client and respx_mock as respx_mock
    # doesn't support custom transports.
    for item in items:
        if "async_client" not in item.fixturenames or "respx_mock" not in item.fixturenames:
            continue

        if not hasattr(item, "callspec"):
            continue

        async_client_param = item.callspec.params.get("async_client")
        if is_dict(async_client_param) and async_client_param.get("http_client") == "aiohttp":
            item.add_marker(pytest.mark.skip(reason="aiohttp client is not compatible with respx_mock"))


@pytest.fixture(autouse=True)
def mock_oauth_token_for_respx(request: FixtureRequest) -> None:
    if "respx_mock" not in request.fixturenames:
        return

    # Ensure a fresh OAuth2 client per test so the token request is made
    # while respx is active and the route is counted as called.
    _clear_oauth2_cache()

    respx_mock = request.getfixturevalue("respx_mock")
    respx_mock.post("https://auth.us-west-2.fragment.dev/oauth2/token").mock(
        return_value=httpx.Response(200, json={"access_token": "test-token", "expires_in": 3600})
    )


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

client_id = "My Client ID"
client_secret = "My Client Secret"


@pytest.fixture()
def client(request: FixtureRequest) -> Iterator[Fragment]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    if "respx_mock" in request.fixturenames:
        _clear_oauth2_cache()

    with Fragment(
        base_url=base_url, client_id=client_id, client_secret=client_secret, _strict_response_validation=strict
    ) as client:
        yield client


@pytest.fixture()
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncFragment]:
    param = getattr(request, "param", True)

    # defaults
    strict = True
    http_client: None | httpx.AsyncClient = None

    if isinstance(param, bool):
        strict = param
    elif is_dict(param):
        strict = param.get("strict", True)
        assert isinstance(strict, bool)

        http_client_type = param.get("http_client", "httpx")
        if http_client_type == "aiohttp":
            http_client = DefaultAioHttpClient()
    else:
        raise TypeError(f"Unexpected fixture parameter type {type(param)}, expected bool or dict")

    if "respx_mock" in request.fixturenames:
        _clear_oauth2_cache()

    async with AsyncFragment(
        base_url=base_url,
        client_id=client_id,
        client_secret=client_secret,
        _strict_response_validation=strict,
        http_client=http_client,
    ) as client:
        yield client
