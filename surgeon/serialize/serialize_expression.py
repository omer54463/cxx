from collections.abc import Iterable

from surgeon.expression.expression import Expression


def serialize_expression(expression: Expression) -> Iterable[str]:
    match expression:
        case _:
            raise TypeError(f"Unexpected type {type(expression)}")


def serialize_optional_expression(expression: Expression | None) -> Iterable[str]:
    if expression is not None:
        yield from serialize_expression(expression)
