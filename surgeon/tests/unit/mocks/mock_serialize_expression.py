from collections.abc import Iterable
from dataclasses import dataclass

import pytest
import pytest_mock

from surgeon.expression.expression import Expression
from surgeon.serialize import (
    serialize_expression as serialize_expression_module,
)
from surgeon.serialize import (
    serialize_statement as serialize_statement_module,
)


@dataclass
class FakeExpression(Expression):
    content: str


def fake_serialize_expression(expression: Expression) -> Iterable[str]:
    assert isinstance(expression, FakeExpression), "Invalid expression type in test"
    yield expression.content


@pytest.fixture()
def mock_serialize_expression(module_mocker: pytest_mock.MockerFixture) -> None:
    for patch_module in (serialize_statement_module, serialize_expression_module):
        module_mocker.patch.object(
            patch_module,
            "serialize_expression",
            wraps=fake_serialize_expression,
        )
