# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import (
    TransactionListResponse,
    TransactionCreateResponse,
    TransactionRetrieveResponse,
)
from fragment._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        transaction = client.transactions.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Fragment) -> None:
        transaction = client.transactions.create(
            account={
                "id": "ext_account_YWJjMTIz",
                "external_id": "acct_external_123",
            },
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        transaction = client.transactions.retrieve(
            "txn_1234567890",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.retrieve(
            "txn_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.retrieve(
            "txn_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        transaction = client.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Fragment) -> None:
        transaction = client.transactions.list(
            account="ext_account_YWJjMTIz",
            reconciliation_status="reconciled",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.create(
            account={
                "id": "ext_account_YWJjMTIz",
                "external_id": "acct_external_123",
            },
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.create(
            account={},
            allocations=[
                {
                    "amount": "1000",
                    "invoice_id": "inv_abc123",
                    "type": "invoice_payin",
                    "user": {"id": "user_abc123"},
                }
            ],
            amount="-1000",
            currency="USD",
            external_id="bank_txn_123",
            posted=parse_datetime("2026-02-12T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionCreateResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.retrieve(
            "txn_1234567890",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.retrieve(
            "txn_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.retrieve(
            "txn_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.list(
            account="ext_account_YWJjMTIz",
            reconciliation_status="reconciled",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
