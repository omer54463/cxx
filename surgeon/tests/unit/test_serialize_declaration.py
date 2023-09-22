from collections.abc import Iterable
from itertools import chain

import pytest

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration
from surgeon.serialize.serialize_declaration import serialize_declaration
from surgeon.tests.unit.mocks.mock_serialize_expression import FakeExpression
from surgeon.tests.unit.mocks.mock_serialize_literal import FakeLiteral

BASIC_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        StaticAssertDeclaration(FakeExpression("expression"), FakeLiteral("literal")),
        [["static_assert", "(", "expression", "literal", ")", ";"]],
    ),
)

DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = chain(
    BASIC_DECLARATION_TEST_DATA,
)


@pytest.mark.usefixtures("mock_serialize_expression", "mock_serialize_literal")
@pytest.mark.parametrize(("declaration", "expected"), DECLARATION_TEST_DATA)
def test_serialize_declaration(
    declaration: Declaration,
    expected: list[list[str]],
) -> None:
    declaration_lines = serialize_declaration(declaration)
    declaration_lines_as_lists = [list(line) for line in declaration_lines]

    assert declaration_lines_as_lists == expected
