from collections.abc import Iterable
from itertools import chain

import pytest

from surgeon.expression.expression import Expression
from surgeon.expression.literal.boolean_literal import BooleanLiteral
from surgeon.expression.literal.character_literal import CharacterLiteral
from surgeon.expression.literal.identifier_literal import IdentifierLiteral
from surgeon.expression.literal.integer_base import IntegerBase
from surgeon.expression.literal.integer_literal import IntegerLiteral
from surgeon.expression.literal.string_literal import StringLiteral
from surgeon.serialize.serialize_expression import serialize_expression

LITERAL_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (BooleanLiteral(True), ["true"]),
    (BooleanLiteral(False), ["false"]),
    (IdentifierLiteral("identifier"), ["identifier"]),
    (IntegerLiteral(0b1010101, IntegerBase.BINARY), ["0b1010101"]),
    (IntegerLiteral(0o707070, IntegerBase.OCTAL), ["0o707070"]),
    (IntegerLiteral(909090, IntegerBase.DECIMAL), ["909090"]),
    (IntegerLiteral(0xF0F0F0, IntegerBase.HEXADECIMAL), ["0xF0F0F0"]),
    (StringLiteral("string"), ['"string"']),
    (StringLiteral("string\nstring"), ['"""string\nstring"""']),
    (CharacterLiteral("c"), ["'c'"]),
)

EXPRESSION_TEST_DATA: Iterable[tuple[Expression, list[str]]] = chain(
    LITERAL_TEST_DATA,
)


@pytest.mark.parametrize(("expression", "expected"), EXPRESSION_TEST_DATA)
def test_serialize_expression(expression: Expression, expected: list[str]) -> None:
    result = list(serialize_expression(expression))

    assert result == expected
