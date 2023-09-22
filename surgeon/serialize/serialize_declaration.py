from collections.abc import Iterable
from itertools import chain

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration
from surgeon.serialize.serialize_expression import serialize_expression
from surgeon.serialize.serialize_literal import serialize_literal


def serialize_declaration(declaration: Declaration) -> Iterable[Iterable[str]]:
    match declaration:
        case StaticAssertDeclaration(expression, literal):
            yield chain(
                ("static_assert", "("),
                serialize_expression(expression),
                serialize_literal(literal),
                (")", ";"),
            )

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_optional_declaration(
    declaration: Declaration | None,
) -> Iterable[Iterable[str]]:
    if declaration is not None:
        yield from serialize_declaration(declaration)
