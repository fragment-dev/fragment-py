# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import ExternalAccountListResponse, ExternalAccountCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        external_account = client.external_accounts.create(
            external_id="ext_acc_123",
            name="Checking Account",
        )
        assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.external_accounts.with_raw_response.create(
            external_id="ext_acc_123",
            name="Checking Account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.external_accounts.with_streaming_response.create(
            external_id="ext_acc_123",
            name="Checking Account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternalAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        external_account = await async_client.external_accounts.create(
            external_id="ext_acc_123",
            name="Checking Account",
        )
        assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.external_accounts.with_raw_response.create(
            external_id="ext_acc_123",
            name="Checking Account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.external_accounts.with_streaming_response.create(
            external_id="ext_acc_123",
            name="Checking Account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccountCreateResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        external_account = await async_client.external_accounts.list()
        assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccountListResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True
