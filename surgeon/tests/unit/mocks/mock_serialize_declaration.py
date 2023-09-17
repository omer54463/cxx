from collections.abc import Iterable
from dataclasses import dataclass

import pytest
import pytest_mock

from surgeon.declaration.declaration import Declaration
from surgeon.serialize import (
    serialize_declaration as serialize_declaration_module,
)
from surgeon.serialize import (
    serialize_statement as serialize_statement_module,
)


@dataclass
class FakeDeclaration(Declaration):
    content: str


def fake_serialize_declaration(declaration: Declaration) -> Iterable[str]:
    assert isinstance(declaration, FakeDeclaration), "Invalid declaration type in test"
    yield declaration.content


@pytest.fixture()
def mock_serialize_declaration(module_mocker: pytest_mock.MockerFixture) -> None:
    for patch_module in (serialize_statement_module, serialize_declaration_module):
        module_mocker.patch.object(
            patch_module,
            "serialize_declaration",
            wraps=fake_serialize_declaration,
        )
