from collections.abc import Iterable
from itertools import chain

from surgeon.declaration.class_declaration.class_access import ClassAccess
from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_definition import ClassDefinition
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum_declaration.enum_declaration import EnumDeclaration
from surgeon.declaration.enum_declaration.enum_definition import EnumDefinition
from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from surgeon.declaration.simple_declaration.simple_definition import SimpleDefinition
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration
from surgeon.serialize.serialize_expression import serialize_expression
from surgeon.serialize.serialize_literal import serialize_literal


def serialize_declaration(declaration: Declaration) -> Iterable[Iterable[str]]:
    match declaration:
        case ClassDeclaration():
            yield from serialize_class_declaration(declaration)

        case EnumDeclaration():
            yield from serialize_enum_declaration(declaration)

        case SimpleDeclaration():
            yield from serialize_simple_declaration(declaration)

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


def serialize_class_declaration(
    declaration: ClassDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case ClassDefinition(
            specifiers,
            struct,
            identifier,
            final,
            bases,
            declaration_blocks,
        ):
            yield chain(
                specifiers,
                ("struct" if struct else "class", identifier),
                ("final",) if final else (),
                serialize_class_parents(bases),
            )
            yield ("{",)
            for declaration_block in declaration_blocks:
                if declaration_block.access is not None:
                    yield (serialize_class_access(declaration_block.access), ":")
                for inner_declaration in declaration_block.declarations:
                    yield from serialize_declaration(inner_declaration)
            yield ("}", ";")

        case ClassDeclaration(specifiers, struct, identifier):
            yield chain(
                specifiers,
                ("struct" if struct else "class", identifier, ";"),
            )

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_enum_declaration(declaration: EnumDeclaration) -> Iterable[Iterable[str]]:
    match declaration:
        case EnumDefinition(specifiers, scoped, identifier, members):
            yield chain(
                specifiers,
                ("enum",),
                ("class",) if scoped else (),
                (identifier,),
            )
            yield ("{",)
            for member in members:
                if member.value is None:
                    yield (member.identifier, ",")
                else:
                    yield chain(
                        (member.identifier, "="),
                        serialize_expression(member.value),
                        (",",),
                    )
            yield ("}")

        case EnumDeclaration(specifiers, scoped, identifier):
            yield chain(
                specifiers,
                ("enum",),
                ("class",) if scoped else (),
                (identifier, ";"),
            )

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_simple_declaration(
    declaration: SimpleDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case SimpleDefinition(specifiers, type, identifier, initializer):
            yield chain(
                specifiers,
                (type, identifier),
                ("=",),
                serialize_expression(initializer),
                (";",),
            )

        case SimpleDeclaration(specifiers, type, identifier):
            yield chain(specifiers, (type, identifier, ";"))


def serialize_class_parents(parents: list[ClassBase]) -> Iterable[str]:
    if len(parents) == 0:
        return

    yield ":"
    for parent in parents:
        if parent.virtual:
            yield "virtual"
        if parent.access is not None:
            yield serialize_class_access(parent.access)
        yield parent.identifier


def serialize_class_access(access: ClassAccess) -> str:
    match access:
        case ClassAccess.PUBLIC:
            return "public"

        case ClassAccess.PROTECTED:
            return "protected"

        case ClassAccess.PRIVATE:
            return "private"

        case _:
            raise TypeError(f"Unexpected type {type(access)}")
