from collections.abc import Iterable

from surgeon.expression.expression import Expression
from surgeon.expression.literal.boolean_literal import BooleanLiteral
from surgeon.expression.literal.character_literal import CharacterLiteral
from surgeon.expression.literal.identifier_literal import IdentifierLiteral
from surgeon.expression.literal.integer_base import IntegerBase
from surgeon.expression.literal.integer_literal import IntegerLiteral
from surgeon.expression.literal.literal import Literal
from surgeon.expression.literal.string_literal import StringLiteral


def serialize_expression(expression: Expression) -> Iterable[str]:
    match expression:
        case Literal():
            yield from serialize_literal(expression)

        case _:
            raise TypeError(f"Unexpected type {type(expression)}")


def serialize_optional_expression(expression: Expression | None) -> Iterable[str]:
    if expression is not None:
        yield from serialize_expression(expression)


def serialize_literal(literal: Literal) -> Iterable[str]:
    match literal:
        case BooleanLiteral(value):
            yield "true" if value else "false"

        case IdentifierLiteral(identifier):
            yield identifier

        case IntegerLiteral():
            yield from serialize_integer_literal(literal)

        case StringLiteral(value):
            quote = '"""' if "\n" in value else '"'
            yield f"{quote}{value}{quote}"

        case CharacterLiteral(value):
            yield f"'{value}'"


def serialize_integer_literal(literal: IntegerLiteral) -> Iterable[str]:
    match literal.base:
        case IntegerBase.BINARY:
            yield bin(literal.value)

        case IntegerBase.OCTAL:
            yield oct(literal.value)

        case IntegerBase.DECIMAL:
            yield str(literal.value)

        case IntegerBase.HEXADECIMAL:
            yield hex(literal.value).upper().replace("X", "x")
