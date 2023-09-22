from collections.abc import Iterable
from itertools import chain

from surgeon.declaration.alias.alias_declaration import AliasDeclaration
from surgeon.declaration.alias.alias_like_declaration import AliasLikeDeclaration
from surgeon.declaration.alias.namespace_alias_declaration import (
    NamespaceAliasDeclaration,
)
from surgeon.declaration.alias.type_def_declaration import TypeDefDeclaration
from surgeon.declaration.alias.using_declaration import UsingDeclaration
from surgeon.declaration.alias.using_enum_declaration import UsingEnumDeclaration
from surgeon.declaration.alias.using_namespace_declaration import (
    UsingNamespaceDeclaration,
)
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

        case AliasLikeDeclaration():
            yield from serialize_alias_like_declaration(declaration)

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_optional_declaration(
    declaration: Declaration | None,
) -> Iterable[Iterable[str]]:
    if declaration is not None:
        yield from serialize_declaration(declaration)


def serialize_alias_like_declaration(
    declaration: AliasLikeDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case AliasDeclaration(new_type, old_type):
            yield ("using", new_type, "=", old_type, ";")

        case NamespaceAliasDeclaration(new_identifier, old_identifier):
            yield ("namespace", new_identifier, "=", old_identifier, ";")

        case UsingDeclaration(identifier):
            yield ("using", identifier, ";")

        case UsingNamespaceDeclaration(identifier):
            yield ("using", "namespace", identifier, ";")

        case UsingEnumDeclaration(identifier):
            yield ("using", "enum", identifier, ";")

        case TypeDefDeclaration(new_type, old_type):
            yield ("typedef", old_type, new_type, ";")

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")
