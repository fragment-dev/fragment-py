# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import PartyListResponse, PartyCreateResponse, PartyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        party = client.parties.create(
            external_id="party_ext_123",
        )
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Fragment) -> None:
        party = client.parties.create(
            external_id="party_ext_123",
            type="buyer",
        )
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.parties.with_raw_response.create(
            external_id="party_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.parties.with_streaming_response.create(
            external_id="party_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert_matches_type(PartyCreateResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        party = client.parties.retrieve(
            "party_ext_123",
        )
        assert_matches_type(PartyRetrieveResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.parties.with_raw_response.retrieve(
            "party_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert_matches_type(PartyRetrieveResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.parties.with_streaming_response.retrieve(
            "party_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert_matches_type(PartyRetrieveResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.parties.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        party = client.parties.list()
        assert_matches_type(PartyListResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = response.parse()
        assert_matches_type(PartyListResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = response.parse()
            assert_matches_type(PartyListResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        party = await async_client.parties.create(
            external_id="party_ext_123",
        )
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFragment) -> None:
        party = await async_client.parties.create(
            external_id="party_ext_123",
            type="buyer",
        )
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.parties.with_raw_response.create(
            external_id="party_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert_matches_type(PartyCreateResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.parties.with_streaming_response.create(
            external_id="party_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert_matches_type(PartyCreateResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        party = await async_client.parties.retrieve(
            "party_ext_123",
        )
        assert_matches_type(PartyRetrieveResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.parties.with_raw_response.retrieve(
            "party_ext_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert_matches_type(PartyRetrieveResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.parties.with_streaming_response.retrieve(
            "party_ext_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert_matches_type(PartyRetrieveResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.parties.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        party = await async_client.parties.list()
        assert_matches_type(PartyListResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.parties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        party = await response.parse()
        assert_matches_type(PartyListResponse, party, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.parties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            party = await response.parse()
            assert_matches_type(PartyListResponse, party, path=["response"])

        assert cast(Any, response.is_closed) is True
