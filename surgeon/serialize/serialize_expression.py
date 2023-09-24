from collections.abc import Iterable

from surgeon.expression.expression import Expression
from surgeon.expression.literal.boolean_literal import BooleanLiteral
from surgeon.expression.literal.character_literal import CharacterLiteral
from surgeon.expression.literal.identifier_literal import IdentifierLiteral
from surgeon.expression.literal.integer_base import IntegerBase
from surgeon.expression.literal.integer_literal import IntegerLiteral
from surgeon.expression.literal.literal import Literal
from surgeon.expression.literal.string_literal import StringLiteral
from surgeon.expression.operator.access_operators import (
    MemberOperator,
)
from surgeon.expression.operator.cast_mode import CastMode
from surgeon.expression.operator.operator import (
    BinaryOperator,
    Operator,
    TrinaryOperator,
    UnaryOperator,
)
from surgeon.expression.operator.other_operators import (
    CastOperator,
    CCastOperator,
    FunctionCallOperator,
)
from surgeon.serialize.operator_precedence import get_precedence
from surgeon.serialize.operator_symbols import (
    BINARY_OPERATOR_SYMBOLS,
    TRINARY_OPERATOR_SYMBOLS,
    UNARY_OPERATOR_SYMBOLS,
)


def serialize_expression(expression: Expression) -> Iterable[str]:
    match expression:
        case Operator():
            yield from serialize_operator(expression)

        case Literal():
            yield from serialize_literal(expression)

        case _:
            raise TypeError(f"Unexpected type {type(expression)}")


def serialize_optional_expression(expression: Expression | None) -> Iterable[str]:
    if expression is not None:
        yield from serialize_expression(expression)


def serialize_precedenced_expression(
    expression: Expression,
    against: Expression | type[Expression],
) -> Iterable[str]:
    if get_precedence(expression) > get_precedence(against):
        yield "("
        yield from serialize_expression(expression)
        yield ")"

    else:
        yield from serialize_expression(expression)


def serialize_operator(operator: Operator) -> Iterable[str]:
    match operator:
        case UnaryOperator():
            yield from serialize_unary_operator(operator)

        case BinaryOperator():
            yield from serialize_binary_operator(operator)

        case TrinaryOperator():
            yield from serialize_trinary_operator(operator)

        case CastOperator():
            yield from serialize_cast_operator(operator)

        case MemberOperator(operand, identifier, dereference):
            yield from serialize_precedenced_expression(operand, MemberOperator)
            yield "->" if dereference else "."
            yield identifier

        case CCastOperator(type, operand):
            yield "("
            yield type
            yield ")"
            yield from serialize_precedenced_expression(operand, CCastOperator)

        case FunctionCallOperator(operand, argument_operands):
            yield from serialize_precedenced_expression(operand, FunctionCallOperator)
            yield "("
            for index, argument_operand in enumerate(argument_operands):
                yield from serialize_expression(argument_operand)
                if index < len(argument_operands) - 1:
                    yield ","
            yield ")"


def serialize_unary_operator(operator: UnaryOperator) -> Iterable[str]:
    symbols = UNARY_OPERATOR_SYMBOLS[type(operator)]

    if symbols.before is not None:
        yield symbols.before

    yield from serialize_precedenced_expression(operator.operand, operator)

    if symbols.after is not None:
        yield symbols.after


def serialize_binary_operator(operator: BinaryOperator) -> Iterable[str]:
    symbols = BINARY_OPERATOR_SYMBOLS[type(operator)]

    if symbols.before is not None:
        yield symbols.before

    yield from serialize_precedenced_expression(operator.left_operand, operator)

    if symbols.between is not None:
        yield symbols.between

    yield from serialize_precedenced_expression(operator.right_operand, operator)

    if symbols.after is not None:
        yield symbols.after


def serialize_trinary_operator(operator: TrinaryOperator) -> Iterable[str]:
    symbols = TRINARY_OPERATOR_SYMBOLS[type(operator)]

    if symbols.before is not None:
        yield symbols.before

    yield from serialize_precedenced_expression(operator.left_operand, operator)

    if symbols.left is not None:
        yield symbols.left

    yield from serialize_precedenced_expression(operator.middle_operand, operator)

    if symbols.right is not None:
        yield symbols.right

    yield from serialize_precedenced_expression(operator.right_operand, operator)

    if symbols.after is not None:
        yield symbols.after


def serialize_cast_operator(operator: CastOperator) -> Iterable[str]:
    match operator.mode:
        case CastMode.STATIC:
            yield "static_cast"

        case CastMode.DYNAMIC:
            yield "dynamic_cast"

        case CastMode.CONST:
            yield "const_cast"

        case CastMode.REINTERPRET:
            yield "reinterpret_cast"

    yield "<"
    yield operator.type
    yield ">"
    yield "("
    yield from serialize_expression(operator.operand)
    yield ")"


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
