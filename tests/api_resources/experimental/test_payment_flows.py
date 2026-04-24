# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types.experimental import (
    PaymentFlowCreateResponse,
    PaymentFlowSearchResponse,
    PaymentFlowRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        payment_flow = client.experimental.payment_flows.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        )
        assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.experimental.payment_flows.with_raw_response.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.experimental.payment_flows.with_streaming_response.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = response.parse()
            assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        payment_flow = client.experimental.payment_flows.retrieve(
            "pf_abc123",
        )
        assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.experimental.payment_flows.with_raw_response.retrieve(
            "pf_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.experimental.payment_flows.with_streaming_response.retrieve(
            "pf_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = response.parse()
            assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_flow_ref` but received ''"):
            client.experimental.payment_flows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Fragment) -> None:
        payment_flow = client.experimental.payment_flows.search()
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Fragment) -> None:
        payment_flow = client.experimental.payment_flows.search(
            invoice_id="invoice_id",
            page_info={
                "after": "after",
                "limit": 0,
            },
        )
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Fragment) -> None:
        response = client.experimental.payment_flows.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = response.parse()
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Fragment) -> None:
        with client.experimental.payment_flows.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = response.parse()
            assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentFlows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        payment_flow = await async_client.experimental.payment_flows.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        )
        assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.experimental.payment_flows.with_raw_response.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = await response.parse()
        assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.experimental.payment_flows.with_streaming_response.create(
            external_id="pf_123",
            invoice={"id": "inv_abc123"},
            type="single_invoice_settlement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = await response.parse()
            assert_matches_type(PaymentFlowCreateResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        payment_flow = await async_client.experimental.payment_flows.retrieve(
            "pf_abc123",
        )
        assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.experimental.payment_flows.with_raw_response.retrieve(
            "pf_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = await response.parse()
        assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.experimental.payment_flows.with_streaming_response.retrieve(
            "pf_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = await response.parse()
            assert_matches_type(PaymentFlowRetrieveResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_flow_ref` but received ''"):
            await async_client.experimental.payment_flows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncFragment) -> None:
        payment_flow = await async_client.experimental.payment_flows.search()
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncFragment) -> None:
        payment_flow = await async_client.experimental.payment_flows.search(
            invoice_id="invoice_id",
            page_info={
                "after": "after",
                "limit": 0,
            },
        )
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncFragment) -> None:
        response = await async_client.experimental.payment_flows.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_flow = await response.parse()
        assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncFragment) -> None:
        async with async_client.experimental.payment_flows.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_flow = await response.parse()
            assert_matches_type(PaymentFlowSearchResponse, payment_flow, path=["response"])

        assert cast(Any, response.is_closed) is True
