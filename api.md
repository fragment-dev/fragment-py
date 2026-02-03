# ExternalPayments

Types:

```python
from fragment.types import (
    ExternalPaymentCreateResponse,
    ExternalPaymentRetrieveResponse,
    ExternalPaymentListResponse,
)
```

Methods:

- <code title="post /external-payments">client.external_payments.<a href="./src/fragment/resources/external_payments.py">create</a>(\*\*<a href="src/fragment/types/external_payment_create_params.py">params</a>) -> <a href="./src/fragment/types/external_payment_create_response.py">ExternalPaymentCreateResponse</a></code>
- <code title="get /external-payments/{transactionId}">client.external_payments.<a href="./src/fragment/resources/external_payments.py">retrieve</a>(transaction_id) -> <a href="./src/fragment/types/external_payment_retrieve_response.py">ExternalPaymentRetrieveResponse</a></code>
- <code title="get /external-payments">client.external_payments.<a href="./src/fragment/resources/external_payments.py">list</a>() -> <a href="./src/fragment/types/external_payment_list_response.py">ExternalPaymentListResponse</a></code>

# Invoices

Types:

```python
from fragment.types import (
    InvoiceCreateResponse,
    InvoiceRetrieveResponse,
    InvoiceUpdateResponse,
    InvoiceListResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">create</a>(\*\*<a href="src/fragment/types/invoice_create_params.py">params</a>) -> <a href="./src/fragment/types/invoice_create_response.py">InvoiceCreateResponse</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">retrieve</a>(id) -> <a href="./src/fragment/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="post /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">update</a>(id, \*\*<a href="src/fragment/types/invoice_update_params.py">params</a>) -> <a href="./src/fragment/types/invoice_update_response.py">InvoiceUpdateResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">list</a>() -> <a href="./src/fragment/types/invoice_list_response.py">InvoiceListResponse</a></code>

# Parties

Types:

```python
from fragment.types import PartyCreateResponse, PartyRetrieveResponse, PartyListResponse
```

Methods:

- <code title="post /parties">client.parties.<a href="./src/fragment/resources/parties.py">create</a>(\*\*<a href="src/fragment/types/party_create_params.py">params</a>) -> <a href="./src/fragment/types/party_create_response.py">PartyCreateResponse</a></code>
- <code title="get /parties/{externalId}">client.parties.<a href="./src/fragment/resources/parties.py">retrieve</a>(external_id) -> <a href="./src/fragment/types/party_retrieve_response.py">PartyRetrieveResponse</a></code>
- <code title="get /parties">client.parties.<a href="./src/fragment/resources/parties.py">list</a>() -> <a href="./src/fragment/types/party_list_response.py">PartyListResponse</a></code>

# Platform

Types:

```python
from fragment.types import PlatformRetrieveResponse, PlatformUpdateResponse
```

Methods:

- <code title="get /platform">client.platform.<a href="./src/fragment/resources/platform.py">retrieve</a>() -> <a href="./src/fragment/types/platform_retrieve_response.py">PlatformRetrieveResponse</a></code>
- <code title="post /platform">client.platform.<a href="./src/fragment/resources/platform.py">update</a>(\*\*<a href="src/fragment/types/platform_update_params.py">params</a>) -> <a href="./src/fragment/types/platform_update_response.py">PlatformUpdateResponse</a></code>

# Products

Types:

```python
from fragment.types import ProductCreateResponse, ProductRetrieveResponse, ProductListResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/fragment/resources/products.py">create</a>(\*\*<a href="src/fragment/types/product_create_params.py">params</a>) -> <a href="./src/fragment/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /products/{code}">client.products.<a href="./src/fragment/resources/products.py">retrieve</a>(code) -> <a href="./src/fragment/types/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="get /products">client.products.<a href="./src/fragment/resources/products.py">list</a>() -> <a href="./src/fragment/types/product_list_response.py">ProductListResponse</a></code>
