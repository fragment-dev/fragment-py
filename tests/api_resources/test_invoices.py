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
    InvoiceSearchResponse,
    InvoiceUpdateResponse,
    InvoiceRetrieveResponse,
    InvoiceListHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        invoice = client.invoices.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Fragment) -> None:
        invoice = client.invoices.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                    "amount": "1000",
                    "currency_code": "USD",
                    "price": {
                        "amount": "1000",
                        "quantity": 2,
                        "unit_price": "500",
                    },
                    "tags": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                }
            ],
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        invoice = client.invoices.retrieve(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.retrieve(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Fragment) -> None:
        invoice = client.invoices.update(
            id="inv_1234567890",
            current_invoice_version=3,
        )
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Fragment) -> None:
        invoice = client.invoices.update(
            id="inv_1234567890",
            current_invoice_version=3,
            line_items={
                "create": [
                    {
                        "description": "Professional services for January 2026",
                        "product_id": "prod_1234567890",
                        "type": "payout",
                        "user": {"id": "user_abc123"},
                        "amount": "1000",
                        "currency_code": "USD",
                        "price": {
                            "amount": "1000",
                            "quantity": 2,
                            "unit_price": "500",
                        },
                        "tags": [
                            {
                                "key": "department",
                                "value": "engineering",
                            }
                        ],
                    }
                ],
                "delete": [{"id": "id"}],
                "update": [
                    {
                        "id": "li_1234567890",
                        "description": "description",
                        "price": {
                            "quantity": 2,
                            "unit_price": "500",
                            "amount": "2000",
                        },
                        "tags": {
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
                    }
                ],
            },
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
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.update(
            id="inv_1234567890",
            current_invoice_version=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.update(
            id="inv_1234567890",
            current_invoice_version=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.update(
                id="",
                current_invoice_version=3,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        invoice = client.invoices.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_history(self, client: Fragment) -> None:
        invoice = client.invoices.list_history(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_history(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.list_history(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_history(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.list_history(
            "inv_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_history(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.invoices.with_raw_response.list_history(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Fragment) -> None:
        invoice = client.invoices.search(
            filter={},
        )
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Fragment) -> None:
        invoice = client.invoices.search(
            filter={
                "status": "open",
                "tags": {
                    "all": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                    "any": [
                        {
                            "key": "department",
                            "value": "eng*",
                        }
                    ],
                },
                "transaction_tags": {
                    "all": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                    "any": [
                        {
                            "key": "department",
                            "value": "eng*",
                        }
                    ],
                },
                "users": {
                    "all": [{"id": "user_abc123"}],
                    "any": [{"id": "user_abc123"}],
                },
            },
            page_info={
                "after": "after",
                "limit": 20,
            },
        )
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Fragment) -> None:
        response = client.invoices.with_raw_response.search(
            filter={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Fragment) -> None:
        with client.invoices.with_streaming_response.search(
            filter={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                    "amount": "1000",
                    "currency_code": "USD",
                    "price": {
                        "amount": "1000",
                        "quantity": 2,
                        "unit_price": "500",
                    },
                    "tags": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                }
            ],
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
        )
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.create(
            invoice_id="invoice_2024_001",
            line_items=[
                {
                    "description": "Professional services for January 2026",
                    "product_id": "prod_1234567890",
                    "type": "payout",
                    "user": {"id": "user_abc123"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceCreateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.retrieve(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.retrieve(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.update(
            id="inv_1234567890",
            current_invoice_version=3,
        )
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.update(
            id="inv_1234567890",
            current_invoice_version=3,
            line_items={
                "create": [
                    {
                        "description": "Professional services for January 2026",
                        "product_id": "prod_1234567890",
                        "type": "payout",
                        "user": {"id": "user_abc123"},
                        "amount": "1000",
                        "currency_code": "USD",
                        "price": {
                            "amount": "1000",
                            "quantity": 2,
                            "unit_price": "500",
                        },
                        "tags": [
                            {
                                "key": "department",
                                "value": "engineering",
                            }
                        ],
                    }
                ],
                "delete": [{"id": "id"}],
                "update": [
                    {
                        "id": "li_1234567890",
                        "description": "description",
                        "price": {
                            "quantity": 2,
                            "unit_price": "500",
                            "amount": "2000",
                        },
                        "tags": {
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
                    }
                ],
            },
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
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.update(
            id="inv_1234567890",
            current_invoice_version=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.update(
            id="inv_1234567890",
            current_invoice_version=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceUpdateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.update(
                id="",
                current_invoice_version=3,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_history(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.list_history(
            "inv_1234567890",
        )
        assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_history(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.list_history(
            "inv_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_history(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.list_history(
            "inv_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListHistoryResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_history(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.invoices.with_raw_response.list_history(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.search(
            filter={},
        )
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncFragment) -> None:
        invoice = await async_client.invoices.search(
            filter={
                "status": "open",
                "tags": {
                    "all": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                    "any": [
                        {
                            "key": "department",
                            "value": "eng*",
                        }
                    ],
                },
                "transaction_tags": {
                    "all": [
                        {
                            "key": "department",
                            "value": "engineering",
                        }
                    ],
                    "any": [
                        {
                            "key": "department",
                            "value": "eng*",
                        }
                    ],
                },
                "users": {
                    "all": [{"id": "user_abc123"}],
                    "any": [{"id": "user_abc123"}],
                },
            },
            page_info={
                "after": "after",
                "limit": 20,
            },
        )
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncFragment) -> None:
        response = await async_client.invoices.with_raw_response.search(
            filter={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncFragment) -> None:
        async with async_client.invoices.with_streaming_response.search(
            filter={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceSearchResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True
