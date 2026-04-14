# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .product import Product
from .._models import BaseModel

__all__ = ["ProductCreateResponse"]


class ProductCreateResponse(BaseModel):
    data: Product
    """Product object."""
