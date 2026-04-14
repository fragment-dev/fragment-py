# ExternalAccounts

Types:

```python
from fragment.types import (
    ExternalAccount,
    ExternalAccountCreateResponse,
    ExternalAccountListResponse,
)
```

Methods:

- <code title="post /external-accounts">client.external_accounts.<a href="./src/fragment/resources/external_accounts.py">create</a>(\*\*<a href="src/fragment/types/external_account_create_params.py">params</a>) -> <a href="./src/fragment/types/external_account_create_response.py">ExternalAccountCreateResponse</a></code>
- <code title="get /external-accounts">client.external_accounts.<a href="./src/fragment/resources/external_accounts.py">list</a>() -> <a href="./src/fragment/types/external_account_list_response.py">ExternalAccountListResponse</a></code>

# Invoices

Types:

```python
from fragment.types import (
    Invoice,
    InvoiceCreateResponse,
    InvoiceRetrieveResponse,
    InvoiceUpdateResponse,
    InvoiceListResponse,
    InvoiceListHistoryResponse,
    InvoiceSearchResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">create</a>(\*\*<a href="src/fragment/types/invoice_create_params.py">params</a>) -> <a href="./src/fragment/types/invoice_create_response.py">InvoiceCreateResponse</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">retrieve</a>(id) -> <a href="./src/fragment/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="patch /invoices/{id}">client.invoices.<a href="./src/fragment/resources/invoices.py">update</a>(id, \*\*<a href="src/fragment/types/invoice_update_params.py">params</a>) -> <a href="./src/fragment/types/invoice_update_response.py">InvoiceUpdateResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/fragment/resources/invoices.py">list</a>() -> <a href="./src/fragment/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="get /invoices/{id}/history">client.invoices.<a href="./src/fragment/resources/invoices.py">list_history</a>(id) -> <a href="./src/fragment/types/invoice_list_history_response.py">InvoiceListHistoryResponse</a></code>
- <code title="post /invoices/search">client.invoices.<a href="./src/fragment/resources/invoices.py">search</a>(\*\*<a href="src/fragment/types/invoice_search_params.py">params</a>) -> <a href="./src/fragment/types/invoice_search_response.py">InvoiceSearchResponse</a></code>

# Products

Types:

```python
from fragment.types import (
    Product,
    ProductCreateResponse,
    ProductRetrieveResponse,
    ProductListResponse,
)
```

Methods:

- <code title="post /products">client.products.<a href="./src/fragment/resources/products.py">create</a>(\*\*<a href="src/fragment/types/product_create_params.py">params</a>) -> <a href="./src/fragment/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /products/{code}">client.products.<a href="./src/fragment/resources/products.py">retrieve</a>(code) -> <a href="./src/fragment/types/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="get /products">client.products.<a href="./src/fragment/resources/products.py">list</a>() -> <a href="./src/fragment/types/product_list_response.py">ProductListResponse</a></code>

# Roles

Types:

```python
from fragment.types import Role, RoleCreateResponse, RoleListResponse
```

Methods:

- <code title="post /roles">client.roles.<a href="./src/fragment/resources/roles.py">create</a>(\*\*<a href="src/fragment/types/role_create_params.py">params</a>) -> <a href="./src/fragment/types/role_create_response.py">RoleCreateResponse</a></code>
- <code title="get /roles">client.roles.<a href="./src/fragment/resources/roles.py">list</a>() -> <a href="./src/fragment/types/role_list_response.py">RoleListResponse</a></code>

# Transactions

Types:

```python
from fragment.types import (
    Transaction,
    TransactionCreateResponse,
    TransactionRetrieveResponse,
    TransactionUpdateResponse,
    TransactionListResponse,
    TransactionListHistoryResponse,
    TransactionSearchResponse,
    TransactionSearchAllocationsResponse,
)
```

Methods:

- <code title="post /transactions">client.transactions.<a href="./src/fragment/resources/transactions.py">create</a>(\*\*<a href="src/fragment/types/transaction_create_params.py">params</a>) -> <a href="./src/fragment/types/transaction_create_response.py">TransactionCreateResponse</a></code>
- <code title="get /transactions/{transaction_ref}">client.transactions.<a href="./src/fragment/resources/transactions.py">retrieve</a>(transaction_ref) -> <a href="./src/fragment/types/transaction_retrieve_response.py">TransactionRetrieveResponse</a></code>
- <code title="patch /transactions/{transaction_ref}">client.transactions.<a href="./src/fragment/resources/transactions.py">update</a>(transaction_ref, \*\*<a href="src/fragment/types/transaction_update_params.py">params</a>) -> <a href="./src/fragment/types/transaction_update_response.py">TransactionUpdateResponse</a></code>
- <code title="get /transactions">client.transactions.<a href="./src/fragment/resources/transactions.py">list</a>(\*\*<a href="src/fragment/types/transaction_list_params.py">params</a>) -> <a href="./src/fragment/types/transaction_list_response.py">TransactionListResponse</a></code>
- <code title="get /transactions/{transaction_ref}/history">client.transactions.<a href="./src/fragment/resources/transactions.py">list_history</a>(transaction_ref) -> <a href="./src/fragment/types/transaction_list_history_response.py">TransactionListHistoryResponse</a></code>
- <code title="post /transactions/search">client.transactions.<a href="./src/fragment/resources/transactions.py">search</a>(\*\*<a href="src/fragment/types/transaction_search_params.py">params</a>) -> <a href="./src/fragment/types/transaction_search_response.py">TransactionSearchResponse</a></code>
- <code title="post /transactions/allocations/search">client.transactions.<a href="./src/fragment/resources/transactions.py">search_allocations</a>(\*\*<a href="src/fragment/types/transaction_search_allocations_params.py">params</a>) -> <a href="./src/fragment/types/transaction_search_allocations_response.py">TransactionSearchAllocationsResponse</a></code>

# Users

Types:

```python
from fragment.types import User, UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/fragment/resources/users.py">create</a>(\*\*<a href="src/fragment/types/user_create_params.py">params</a>) -> <a href="./src/fragment/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/fragment/resources/users.py">list</a>() -> <a href="./src/fragment/types/user_list_response.py">UserListResponse</a></code>
