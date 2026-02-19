# ExternalAccounts

Types:

```python
from fragment.types import ExternalAccountCreateResponse, ExternalAccountListResponse
```

Methods:

- <code title="post /external-accounts">client.external_accounts.<a href="./src/fragment/resources/external_accounts.py">create</a>(\*\*<a href="src/fragment/types/external_account_create_params.py">params</a>) -> <a href="./src/fragment/types/external_account_create_response.py">ExternalAccountCreateResponse</a></code>
- <code title="get /external-accounts">client.external_accounts.<a href="./src/fragment/resources/external_accounts.py">list</a>() -> <a href="./src/fragment/types/external_account_list_response.py">ExternalAccountListResponse</a></code>

# Invoices

Types:

```python
from fragment.types import (
    InvoiceCreateResponse,
    InvoiceRetrieveResponse,
    InvoiceUpdateResponse,
    InvoiceListResponse,
    InvoiceListHistoryResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">create</a>(\*\*<a href="src/fragment/types/invoice_create_params.py">params</a>) -> <a href="./src/fragment/types/invoice_create_response.py">InvoiceCreateResponse</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">retrieve</a>(id) -> <a href="./src/fragment/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="post /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">update</a>(id, \*\*<a href="src/fragment/types/invoice_update_params.py">params</a>) -> <a href="./src/fragment/types/invoice_update_response.py">InvoiceUpdateResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">list</a>() -> <a href="./src/fragment/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="get /invoices/{id}/history">client.invoices.<a href="./src/fragment/resources/invoices.py">list_history</a>(id) -> <a href="./src/fragment/types/invoice_list_history_response.py">InvoiceListHistoryResponse</a></code>

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

# Roles

Types:

```python
from fragment.types import RoleCreateResponse, RoleListResponse
```

Methods:

- <code title="post /roles">client.roles.<a href="./src/fragment/resources/roles.py">create</a>(\*\*<a href="src/fragment/types/role_create_params.py">params</a>) -> <a href="./src/fragment/types/role_create_response.py">RoleCreateResponse</a></code>
- <code title="get /roles">client.roles.<a href="./src/fragment/resources/roles.py">list</a>() -> <a href="./src/fragment/types/role_list_response.py">RoleListResponse</a></code>

# Transactions

Types:

```python
from fragment.types import TransactionCreateResponse, TransactionListResponse
```

Methods:

- <code title="post /transactions">client.transactions.<a href="./src/fragment/resources/transactions.py">create</a>(\*\*<a href="src/fragment/types/transaction_create_params.py">params</a>) -> <a href="./src/fragment/types/transaction_create_response.py">TransactionCreateResponse</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/fragment/resources/transactions.py">list</a>(\*\*<a href="src/fragment/types/transaction_list_params.py">params</a>) -> <a href="./src/fragment/types/transaction_list_response.py">TransactionListResponse</a></code>

# Users

Types:

```python
from fragment.types import UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/fragment/resources/users.py">create</a>(\*\*<a href="src/fragment/types/user_create_params.py">params</a>) -> <a href="./src/fragment/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/fragment/resources/users.py">list</a>() -> <a href="./src/fragment/types/user_list_response.py">UserListResponse</a></code>
