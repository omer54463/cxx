from collections.abc import Iterable

from surgeon.declaration.alias_declaration.alias_declaration import AliasDeclaration
from surgeon.declaration.alias_declaration.alias_mode import AliasMode
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
from surgeon.declaration.using_declaration.using_declaration import UsingDeclaration
from surgeon.declaration.using_declaration.using_mode import UsingMode


def serialize_declaration(declaration: Declaration) -> Iterable[str]:
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

        case AliasDeclaration():
            yield from serialize_alias_declaration(declaration)

        case UsingDeclaration():
            yield from serialize_using_declaration(declaration)

        case StaticAssertDeclaration(expression, message):
            yield "static_assert"
            yield "("
            yield from serialize_expression(expression)
            yield ","
            yield from serialize_expression(message)
            yield ")"
            yield ";"


def serialize_optional_declaration(declaration: Declaration | None) -> Iterable[str]:
    if declaration is not None:
        yield from serialize_declaration(declaration)


def serialize_class_declaration(declaration: ClassDeclaration) -> Iterable[str]:
    yield from declaration.specifiers
    yield "struct" if declaration.struct else "class"
    yield declaration.identifier

    if isinstance(declaration, ClassDefinition):
        if declaration.final:
            yield "final"
        yield from serialize_class_parents(declaration.bases)

        yield "{"

        for declaration_block in declaration.declaration_blocks:
            if declaration_block.access is not None:
                yield serialize_class_access(declaration_block.access)
                yield ":"

            for inner_declaration in declaration_block.declarations:
                yield from serialize_declaration(inner_declaration)

        yield "}"

    yield ";"


def serialize_enum_declaration(declaration: EnumDeclaration) -> Iterable[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    yield from declaration.specifiers
    yield "enum"
    if declaration.scoped:
        yield "class"
    yield declaration.identifier

    if isinstance(declaration, EnumDefinition):
        yield "{"

        for member in declaration.members:
            if member.value is None:
                yield member.identifier
                yield ","

            else:
                yield member.identifier
                yield "="
                yield from serialize_expression(member.value)
                yield ","

        yield "}"

    yield ";"


def serialize_function_declaration(declaration: FunctionDeclaration) -> Iterable[str]:
    from surgeon.serialize.serialize_statement import serialize_statement

    yield from declaration.specifiers
    yield declaration.return_type
    yield declaration.identifier
    yield from serialize_function_arguments(declaration.arguments)

    if isinstance(declaration, FunctionDefinition):
        yield from serialize_constructor_initializers(declaration.initializers)
        yield "{"
        for statement in declaration.statements:
            yield from serialize_statement(statement)
        yield "}"

    else:
        yield ";"


def serialize_simple_declaration(declaration: SimpleDeclaration) -> Iterable[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    yield from declaration.specifiers
    yield declaration.type
    yield declaration.identifier

    if isinstance(declaration, SimpleDefinition):
        yield "="
        yield from serialize_expression(declaration.value)

    yield ";"


def serialize_namespace_declaration(declaration: NamespaceDeclaration) -> Iterable[str]:
    yield from declaration.specificers
    yield "namespace"
    yield declaration.identifier

    if isinstance(declaration, NamespaceDefinition):
        yield "{"
        for inner_declaration in declaration.declarations:
            yield from serialize_declaration(inner_declaration)
        yield "}"

    else:
        yield ";"


def serialize_alias_declaration(declaration: AliasDeclaration) -> Iterable[str]:
    match declaration.mode:
        case AliasMode.DEFAULT:
            yield "using"
            yield declaration.new_identifier
            yield "="
            yield declaration.old_identifier

        case AliasMode.NAMESPACE:
            yield "namespace"
            yield declaration.new_identifier
            yield "="
            yield declaration.old_identifier

        case AliasMode.TYPE_DEF:
            yield "typedef"
            yield declaration.old_identifier
            yield declaration.new_identifier

    yield ";"


def serialize_using_declaration(declaration: UsingDeclaration) -> Iterable[str]:
    yield "using"

    match declaration.mode:
        case UsingMode.ENUM:
            yield "enum"

        case UsingMode.NAMESPACE:
            yield "namespace"

    yield declaration.identifier
    yield ";"


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
