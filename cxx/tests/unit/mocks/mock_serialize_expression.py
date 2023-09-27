from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from types import ModuleType

import pytest
import pytest_mock

from cxx.expression.expression import Expression


@dataclass
class FakeExpression(Expression):
    content: str


def fake_serialize_expression(expression: Expression) -> Iterator[str]:
    assert isinstance(expression, FakeExpression), "Invalid expression type in test"
    yield expression.content


@pytest.fixture()
def mock_serialize_expression(
    serialization_modules: Iterable[ModuleType],
    module_mocker: pytest_mock.MockerFixture,
) -> None:
    for module in serialization_modules:
        if not hasattr(module, "serialize_expression"):
            continue

        module_mocker.patch.object(
            module,
            "serialize_expression",
            wraps=fake_serialize_expression,
        )
