# Invoices

Types:

```python
from fragment_py.types import (
    InvoiceCreateResponse,
    InvoiceRetrieveResponse,
    InvoiceUpdateResponse,
    InvoiceListResponse,
    InvoiceListHistoryResponse,
)
```

Methods:

- <code title="post /invoices">client.invoices.<a href="./src/fragment_py/resources/invoices.py">create</a>(\*\*<a href="src/fragment_py/types/invoice_create_params.py">params</a>) -> <a href="./src/fragment_py/types/invoice_create_response.py">InvoiceCreateResponse</a></code>
- <code title="get /invoices/{id}">client.invoices.<a href="./src/fragment_py/resources/invoices.py">retrieve</a>(id) -> <a href="./src/fragment_py/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="post /invoices/{id}">client.invoices.<a href="./src/fragment_py/resources/invoices.py">update</a>(id, \*\*<a href="src/fragment_py/types/invoice_update_params.py">params</a>) -> <a href="./src/fragment_py/types/invoice_update_response.py">InvoiceUpdateResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/fragment_py/resources/invoices.py">list</a>() -> <a href="./src/fragment_py/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="get /invoices/{id}/history">client.invoices.<a href="./src/fragment_py/resources/invoices.py">list_history</a>(id) -> <a href="./src/fragment_py/types/invoice_list_history_response.py">InvoiceListHistoryResponse</a></code>

# Platform

Types:

```python
from fragment_py.types import PlatformRetrieveResponse, PlatformUpdateResponse
```

Methods:

- <code title="get /platform">client.platform.<a href="./src/fragment_py/resources/platform.py">retrieve</a>() -> <a href="./src/fragment_py/types/platform_retrieve_response.py">PlatformRetrieveResponse</a></code>
- <code title="post /platform">client.platform.<a href="./src/fragment_py/resources/platform.py">update</a>(\*\*<a href="src/fragment_py/types/platform_update_params.py">params</a>) -> <a href="./src/fragment_py/types/platform_update_response.py">PlatformUpdateResponse</a></code>

# Products

Types:

```python
from fragment_py.types import ProductCreateResponse, ProductRetrieveResponse, ProductListResponse
```

Methods:

- <code title="post /products">client.products.<a href="./src/fragment_py/resources/products.py">create</a>(\*\*<a href="src/fragment_py/types/product_create_params.py">params</a>) -> <a href="./src/fragment_py/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /products/{code}">client.products.<a href="./src/fragment_py/resources/products.py">retrieve</a>(code) -> <a href="./src/fragment_py/types/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="get /products">client.products.<a href="./src/fragment_py/resources/products.py">list</a>() -> <a href="./src/fragment_py/types/product_list_response.py">ProductListResponse</a></code>

# Users

Types:

```python
from fragment_py.types import UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/fragment_py/resources/users.py">create</a>(\*\*<a href="src/fragment_py/types/user_create_params.py">params</a>) -> <a href="./src/fragment_py/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /users">client.users.<a href="./src/fragment_py/resources/users.py">list</a>() -> <a href="./src/fragment_py/types/user_list_response.py">UserListResponse</a></code>
