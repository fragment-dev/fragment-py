# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from fragment import Fragment, AsyncFragment
from tests.utils import assert_matches_type
from fragment.types import (
    ExternalPaymentListResponse,
    ExternalPaymentCreateResponse,
    ExternalPaymentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Fragment) -> None:
        external_payment = client.external_payments.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        )
        assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Fragment) -> None:
        response = client.external_payments.with_raw_response.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Fragment) -> None:
        with client.external_payments.with_streaming_response.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Fragment) -> None:
        external_payment = client.external_payments.retrieve(
            "txn_external_123",
        )
        assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Fragment) -> None:
        response = client.external_payments.with_raw_response.retrieve(
            "txn_external_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Fragment) -> None:
        with client.external_payments.with_streaming_response.retrieve(
            "txn_external_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Fragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.external_payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Fragment) -> None:
        external_payment = client.external_payments.list()
        assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Fragment) -> None:
        response = client.external_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Fragment) -> None:
        with client.external_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternalPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFragment) -> None:
        external_payment = await async_client.external_payments.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        )
        assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFragment) -> None:
        response = await async_client.external_payments.with_raw_response.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = await response.parse()
        assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFragment) -> None:
        async with async_client.external_payments.with_streaming_response.create(
            account_reference="ACC-2024-001",
            amount="50000",
            counterparty_id="party_ext_789",
            currency_code="USD",
            invoice_id="inv_1234567890",
            transaction_id="txn_external_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPaymentCreateResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFragment) -> None:
        external_payment = await async_client.external_payments.retrieve(
            "txn_external_123",
        )
        assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFragment) -> None:
        response = await async_client.external_payments.with_raw_response.retrieve(
            "txn_external_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = await response.parse()
        assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFragment) -> None:
        async with async_client.external_payments.with_streaming_response.retrieve(
            "txn_external_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPaymentRetrieveResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFragment) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.external_payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFragment) -> None:
        external_payment = await async_client.external_payments.list()
        assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFragment) -> None:
        response = await async_client.external_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = await response.parse()
        assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFragment) -> None:
        async with async_client.external_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPaymentListResponse, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True
