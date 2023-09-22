from collections.abc import Iterable

from surgeon.literal.literal import Literal


def serialize_literal(literal: Literal) -> Iterable[str]:
    match literal:
        case _:
            raise TypeError(f"Unexpected type {type(literal)}")


def serialize_optional_literal(literal: Literal | None) -> Iterable[str]:
    if literal is not None:
        yield from serialize_literal(literal)
