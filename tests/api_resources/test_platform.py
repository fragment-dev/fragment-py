# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import PlatformUpdateResponse, PlatformRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlatform:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        platform = client.platform.retrieve()
        assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.platform.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        platform = response.parse()
        assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.platform.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            platform = response.parse()
            assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Fragment) -> None:
        platform = client.platform.update(
            display_name="Acme Corp",
        )
        assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Fragment) -> None:
        response = client.platform.with_raw_response.update(
            display_name="Acme Corp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        platform = response.parse()
        assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Fragment) -> None:
        with client.platform.with_streaming_response.update(
            display_name="Acme Corp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            platform = response.parse()
            assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlatform:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        platform = await async_client.platform.retrieve()
        assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.platform.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        platform = await response.parse()
        assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.platform.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            platform = await response.parse()
            assert_matches_type(PlatformRetrieveResponse, platform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFragment) -> None:
        platform = await async_client.platform.update(
            display_name="Acme Corp",
        )
        assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFragment) -> None:
        response = await async_client.platform.with_raw_response.update(
            display_name="Acme Corp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        platform = await response.parse()
        assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFragment) -> None:
        async with async_client.platform.with_streaming_response.update(
            display_name="Acme Corp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            platform = await response.parse()
            assert_matches_type(PlatformUpdateResponse, platform, path=["response"])

        assert cast(Any, response.is_closed) is True
