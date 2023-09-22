from collections.abc import Iterable
from dataclasses import dataclass
from types import ModuleType

import pytest
import pytest_mock

from surgeon.literal.literal import Literal


@dataclass
class FakeLiteral(Literal):
    content: str


def fake_serialize_literal(literal: Literal) -> Iterable[str]:
    assert isinstance(literal, FakeLiteral), "Invalid literal type in test"
    yield literal.content


@pytest.fixture()
def mock_serialize_literal(
    serialization_modules: Iterable[ModuleType],
    module_mocker: pytest_mock.MockerFixture,
) -> None:
    for module in serialization_modules:
        if not hasattr(module, "serialize_literal"):
            continue

        module_mocker.patch.object(
            module,
            "serialize_literal",
            wraps=fake_serialize_literal,
        )
