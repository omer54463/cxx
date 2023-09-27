from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from types import ModuleType

import pytest
import pytest_mock

from cxx.statement.statement import Statement


@dataclass
class FakeStatement(Statement):
    content: str


def fake_serialize_statement(statement: Statement) -> Iterator[str]:
    assert isinstance(statement, FakeStatement), "Invalid statement type in test"
    yield statement.content
    yield ";"


@pytest.fixture()
def mock_serialize_statement(
    serialization_modules: Iterable[ModuleType],
    module_mocker: pytest_mock.MockerFixture,
) -> None:
    for module in serialization_modules:
        if not hasattr(module, "serialize_statement"):
            continue

        module_mocker.patch.object(
            module,
            "serialize_statement",
            wraps=fake_serialize_statement,
        )
