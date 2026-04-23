# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import RoleListResponse, RoleCreateResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            role = client.roles.create(
                role="admin",
            )

        assert_matches_type(RoleCreateResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.roles.with_raw_response.create(
                role="admin",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleCreateResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            with client.roles.with_streaming_response.create(
                role="admin",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                role = response.parse()
                assert_matches_type(RoleCreateResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            role = client.roles.list()

        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with pytest.warns(DeprecationWarning):
            with client.roles.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                role = response.parse()
                assert_matches_type(RoleListResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            role = await async_client.roles.create(
                role="admin",
            )

        assert_matches_type(RoleCreateResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.roles.with_raw_response.create(
                role="admin",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleCreateResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.roles.with_streaming_response.create(
                role="admin",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                role = await response.parse()
                assert_matches_type(RoleCreateResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            role = await async_client.roles.list()

        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.roles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.roles.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                role = await response.parse()
                assert_matches_type(RoleListResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True
