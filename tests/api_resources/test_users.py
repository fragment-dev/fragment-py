# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import (
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        user = client.users.create(
            external_id="user_ext_123",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Fragment) -> None:
        user = client.users.create(
            external_id="user_ext_123",
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.users.with_raw_response.create(
            external_id="user_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.users.with_streaming_response.create(
            external_id="user_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Fragment) -> None:
        user = client.users.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Fragment) -> None:
        user = client.users.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={
                "create": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
                "delete": [{"key": "key"}],
                "set": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
                "update": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
            },
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Fragment) -> None:
        response = client.users.with_raw_response.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Fragment) -> None:
        with client.users.with_streaming_response.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_ref` but received ''"):
            client.users.with_raw_response.update(
                user_ref="",
                tags={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        user = await async_client.users.create(
            external_id="user_ext_123",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFragment) -> None:
        user = await async_client.users.create(
            external_id="user_ext_123",
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.users.with_raw_response.create(
            external_id="user_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.users.with_streaming_response.create(
            external_id="user_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFragment) -> None:
        user = await async_client.users.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFragment) -> None:
        user = await async_client.users.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={
                "create": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
                "delete": [{"key": "key"}],
                "set": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
                "update": [
                    {
                        "key": "department",
                        "value": "engineering",
                    }
                ],
            },
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFragment) -> None:
        response = await async_client.users.with_raw_response.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFragment) -> None:
        async with async_client.users.with_streaming_response.update(
            user_ref="user_dXNyX2ZyYWdfMDAx",
            tags={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_ref` but received ''"):
            await async_client.users.with_raw_response.update(
                user_ref="",
                tags={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
