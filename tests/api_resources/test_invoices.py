# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import (
    InvoiceListResponse,
    InvoiceCreateResponse,
    InvoiceUpdateResponse,
    InvoiceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        invoice = client.invoices.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Fragment) -> None:
        invoice = client.invoices.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
            status="active",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        invoice = client.invoices.retrieve(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.retrieve(
            "inv_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Fragment) -> None:
        invoice = client.invoices.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        )
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.update(
                id="",
                line_items_update=[
                    {
                        "amount": "1000",
                        "currency_code": "USD",
                        "description": "Professional services for January 2026",
                        "op": "add",
                        "payout_party": {"platform": True},
                        "product_id": "prod_1234567890",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        invoice = client.invoices.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
            status="active",
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.create(
            buyer_party="party_ext_789",
            invoice_id="invoice_2024_001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.retrieve(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.retrieve(
            "inv_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        )
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.update(
            id="inv_1234567890",
            line_items_update=[
                {
                    "amount": "1000",
                    "currency_code": "USD",
                    "description": "Professional services for January 2026",
                    "op": "add",
                    "payout_party": {"platform": True},
                    "product_id": "prod_1234567890",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.update(
                id="",
                line_items_update=[
                    {
                        "amount": "1000",
                        "currency_code": "USD",
                        "description": "Professional services for January 2026",
                        "op": "add",
                        "payout_party": {"platform": True},
                        "product_id": "prod_1234567890",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True
