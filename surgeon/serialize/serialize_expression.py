from collections.abc import Iterable

from surgeon.expression.expression import Expression
from surgeon.expression.raw_expression import RawExpression


def serialize_expression(expression: Expression) -> Iterable[str]:
    match expression:
        case RawExpression(content):
            yield content


def serialize_optional_expression(expression: Expression | None) -> Iterable[str]:
    if expression is not None:
        yield from serialize_expression(expression)
