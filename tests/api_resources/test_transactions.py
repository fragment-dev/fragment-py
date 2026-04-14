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
    TransactionSearchResponse,
    TransactionUpdateResponse,
    TransactionRetrieveResponse,
    TransactionListHistoryResponse,
    TransactionSearchAllocationsResponse,
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            "txn_abc123",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.retrieve(
            "txn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.retrieve(
            "txn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            client.transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Fragment) -> None:
        transaction = client.transactions.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        )
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Fragment) -> None:
        transaction = client.transactions.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
            allocations={
                "create": [
                    {
                        "amount": "1000",
                        "invoice_id": "inv_abc123",
                        "type": "invoice_payin",
                        "user": {"id": "user_abc123"},
                    }
                ],
                "update": [
                    {
                        "id": "alloc_abc123",
                        "amount": "2000",
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
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            client.transactions.with_raw_response.update(
                transaction_ref="",
                current_transaction_version=0,
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_history(self, client: Fragment) -> None:
        transaction = client.transactions.list_history(
            "txn_abc123",
        )
        assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_history(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.list_history(
            "txn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_history(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.list_history(
            "txn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_history(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            client.transactions.with_raw_response.list_history(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Fragment) -> None:
        transaction = client.transactions.search(
            filter={},
        )
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Fragment) -> None:
        transaction = client.transactions.search(
            filter={
                "account": {
                    "any": [
                        {
                            "id": "ext_account_YWJjMTIz",
                            "external_id": "acct_external_123",
                        }
                    ]
                },
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
            },
            page_info={
                "after": "after",
                "limit": 20,
            },
        )
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.search(
            filter={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.search(
            filter={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_allocations(self, client: Fragment) -> None:
        transaction = client.transactions.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        )
        assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_allocations(self, client: Fragment) -> None:
        response = client.transactions.with_raw_response.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_allocations(self, client: Fragment) -> None:
        with client.transactions.with_streaming_response.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
            tags=[
                {
                    "key": "department",
                    "value": "engineering",
                }
            ],
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            posted=parse_datetime("2024-01-13T00:00:00Z"),
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
            "txn_abc123",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.retrieve(
            "txn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.retrieve(
            "txn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            await async_client.transactions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        )
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
            allocations={
                "create": [
                    {
                        "amount": "1000",
                        "invoice_id": "inv_abc123",
                        "type": "invoice_payin",
                        "user": {"id": "user_abc123"},
                    }
                ],
                "update": [
                    {
                        "id": "alloc_abc123",
                        "amount": "2000",
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
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.update(
            transaction_ref="txn_abc123",
            current_transaction_version=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionUpdateResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            await async_client.transactions.with_raw_response.update(
                transaction_ref="",
                current_transaction_version=0,
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_history(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.list_history(
            "txn_abc123",
        )
        assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_history(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.list_history(
            "txn_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_history(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.list_history(
            "txn_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListHistoryResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_history(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_ref` but received ''"):
            await async_client.transactions.with_raw_response.list_history(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.search(
            filter={},
        )
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.search(
            filter={
                "account": {
                    "any": [
                        {
                            "id": "ext_account_YWJjMTIz",
                            "external_id": "acct_external_123",
                        }
                    ]
                },
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
            },
            page_info={
                "after": "after",
                "limit": 20,
            },
        )
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.search(
            filter={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.search(
            filter={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSearchResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_allocations(self, async_client: AsyncFragment) -> None:
        transaction = await async_client.transactions.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        )
        assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_allocations(self, async_client: AsyncFragment) -> None:
        response = await async_client.transactions.with_raw_response.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_allocations(self, async_client: AsyncFragment) -> None:
        async with async_client.transactions.with_streaming_response.search_allocations(
            filter={"invoice_id": {"any": ["inv_abc123"]}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSearchAllocationsResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
