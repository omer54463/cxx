from collections.abc import Iterable
from importlib import import_module
from pkgutil import iter_modules
from re import compile
from types import ModuleType

import pytest

from cxx import serialize

SERIALIZE_REGEX = compile(r"^serialize_.*")


@pytest.fixture()
def serialization_modules() -> Iterable[ModuleType]:
    return tuple(
        import_module(f"{serialize.__name__}.{info.name}")
        for info in iter_modules(serialize.__path__)
        if SERIALIZE_REGEX.match(info.name)
    )
