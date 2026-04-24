# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types.experimental import PaymentSearchResponse, PaymentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        payment = client.experimental.payments.retrieve(
            "pmt_abc123",
        )
        assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.experimental.payments.with_raw_response.retrieve(
            "pmt_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.experimental.payments.with_streaming_response.retrieve(
            "pmt_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_ref` but received ''"):
            client.experimental.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Fragment) -> None:
        payment = client.experimental.payments.search()
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Fragment) -> None:
        payment = client.experimental.payments.search(
            page_info={
                "after": "after",
                "limit": 0,
            },
            payment_flow_id="payment_flow_id",
        )
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Fragment) -> None:
        response = client.experimental.payments.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Fragment) -> None:
        with client.experimental.payments.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSearchResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        payment = await async_client.experimental.payments.retrieve(
            "pmt_abc123",
        )
        assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.experimental.payments.with_raw_response.retrieve(
            "pmt_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.experimental.payments.with_streaming_response.retrieve(
            "pmt_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRetrieveResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_ref` but received ''"):
            await async_client.experimental.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncFragment) -> None:
        payment = await async_client.experimental.payments.search()
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncFragment) -> None:
        payment = await async_client.experimental.payments.search(
            page_info={
                "after": "after",
                "limit": 0,
            },
            payment_flow_id="payment_flow_id",
        )
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncFragment) -> None:
        response = await async_client.experimental.payments.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSearchResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncFragment) -> None:
        async with async_client.experimental.payments.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSearchResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
