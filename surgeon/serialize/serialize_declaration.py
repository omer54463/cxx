from collections.abc import Iterable
from itertools import chain

from surgeon.declaration.class_declaration.class_access import ClassAccess
from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_definition import ClassDefinition
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum_declaration.enum_declaration import EnumDeclaration
from surgeon.declaration.enum_declaration.enum_definition import EnumDefinition
from surgeon.declaration.function_declaration.constructor_initializer import (
    ConstructorInitializer,
)
from surgeon.declaration.function_declaration.function_argument import FunctionArgument
from surgeon.declaration.function_declaration.function_declaration import (
    FunctionDeclaration,
)
from surgeon.declaration.function_declaration.function_definition import (
    FunctionDefinition,
)
from surgeon.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)
from surgeon.declaration.namespace_declaration.namespace_definition import (
    NamespaceDefinition,
)
from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from surgeon.declaration.simple_declaration.simple_definition import SimpleDefinition
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration


def serialize_declaration(declaration: Declaration) -> Iterable[Iterable[str]]:
    from surgeon.serialize.serialize_expression import serialize_expression

    match declaration:
        case ClassDeclaration():
            yield from serialize_class_declaration(declaration)

        case EnumDeclaration():
            yield from serialize_enum_declaration(declaration)

        case FunctionDeclaration():
            yield from serialize_function_declaration(declaration)

        case SimpleDeclaration():
            yield from serialize_simple_declaration(declaration)

        case NamespaceDeclaration():
            yield from serialize_namespace_declaration(declaration)

        case StaticAssertDeclaration(expression, message):
            yield chain(
                ("static_assert", "("),
                serialize_expression(expression),
                serialize_expression(message),
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
    from surgeon.serialize.serialize_expression import serialize_expression

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


def serialize_function_declaration(
    declaration: FunctionDeclaration,
) -> Iterable[Iterable[str]]:
    from surgeon.serialize.serialize_statement import serialize_statement

    match declaration:
        case FunctionDefinition(
            specifiers,
            return_type,
            identifier,
            arguments,
            initializers,
            statements,
        ):
            yield chain(
                specifiers,
                (return_type, identifier),
                serialize_function_arguments(arguments),
                serialize_constructor_initializers(initializers),
            )
            yield ("{",)
            for statement in statements:
                yield from serialize_statement(statement)
            yield ("}",)

        case FunctionDeclaration(specifiers, return_type, identifier, arguments):
            yield chain(
                specifiers,
                (return_type, identifier),
                serialize_function_arguments(arguments),
                ";",
            )

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_simple_declaration(
    declaration: SimpleDeclaration,
) -> Iterable[Iterable[str]]:
    from surgeon.serialize.serialize_expression import serialize_expression

    match declaration:
        case SimpleDefinition(specifiers, type_, identifier, initializer):
            yield chain(
                specifiers,
                (type_, identifier),
                ("=",),
                serialize_expression(initializer),
                (";",),
            )

        case SimpleDeclaration(specifiers, type_, identifier):
            yield chain(specifiers, (type_, identifier, ";"))

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_namespace_declaration(
    declaration: NamespaceDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case NamespaceDefinition(specificers, identifier, declarations):
            yield chain(specificers, ("namespace", identifier))
            yield ("{",)
            for inner_declaration in declarations:
                yield from serialize_declaration(inner_declaration)
            yield ("}",)

        case NamespaceDeclaration(specificers, identifier):
            yield chain(specificers, ("namespace", identifier, ";"))

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


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


def serialize_function_arguments(arguments: list[FunctionArgument]) -> Iterable[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    yield "("
    for index, argument in enumerate(arguments):
        yield argument.type
        if argument.identifier is not None:
            yield argument.identifier
        if argument.default is not None:
            yield "="
            yield from serialize_expression(argument.default)
        if index < len(arguments) - 1:
            yield ","
    yield ")"


def serialize_constructor_initializers(
    initializers: list[ConstructorInitializer],
) -> Iterable[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    if len(initializers) == 0:
        return

    yield ":"
    for index, initializer in enumerate(initializers):
        yield initializer.identifier
        yield "("
        yield from serialize_expression(initializer.expression)
        yield ")"
        if index < len(initializers) - 1:
            yield ","
