from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `fragment_py.resources` module.

    This is used so that we can lazily import `fragment_py.resources` only when
    needed *and* so that users can just import `fragment_py` and reference `fragment_py.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("fragment_py.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
