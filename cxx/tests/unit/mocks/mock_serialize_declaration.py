from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from types import ModuleType

import pytest
import pytest_mock

from cxx.declaration.declaration import Declaration


@dataclass
class FakeDeclaration(Declaration):
    content: str


def fake_serialize_declaration(declaration: Declaration) -> Iterator[str]:
    assert isinstance(declaration, FakeDeclaration), "Invalid declaration type in test"
    yield declaration.content
    yield ";"


@pytest.fixture()
def mock_serialize_declaration(
    serialization_modules: Iterable[ModuleType],
    module_mocker: pytest_mock.MockerFixture,
) -> None:
    for module in serialization_modules:
        if not hasattr(module, "serialize_declaration"):
            continue

        module_mocker.patch.object(
            module,
            "serialize_declaration",
            wraps=fake_serialize_declaration,
        )
