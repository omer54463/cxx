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
from surgeon.declaration.clazz.class_access import ClassAccess
from surgeon.declaration.clazz.class_declaration import ClassDeclaration
from surgeon.declaration.clazz.class_definition import ClassDefinition
from surgeon.declaration.clazz.class_like_declaration import ClassLikeDeclaration
from surgeon.declaration.clazz.class_parent import ClassParent
from surgeon.declaration.clazz.final_class_definition import FinalClassDefinition
from surgeon.declaration.clazz.final_struct_definition import FinalStructDefinition
from surgeon.declaration.clazz.struct_declaration import StructDeclaration
from surgeon.declaration.clazz.struct_definition import StructDefinition
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum.enum_declaration import EnumDeclaration
from surgeon.declaration.enum.enum_definition import EnumDefinition
from surgeon.declaration.enum.enum_like_declaration import EnumLikeDeclaration
from surgeon.declaration.enum.scoped_enum_declaration import ScopedEnumDeclaration
from surgeon.declaration.enum.scoped_enum_definition import ScopedEnumDefinition
from surgeon.declaration.specifier import Specifier
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration
from surgeon.serialize.serialize_expression import serialize_expression
from surgeon.serialize.serialize_literal import serialize_literal


def serialize_declaration(declaration: Declaration) -> Iterable[Iterable[str]]:
    match declaration:
        case AliasLikeDeclaration():
            yield from serialize_alias_like_declaration(declaration)

        case ClassLikeDeclaration():
            yield from serialize_class_like_declaration(declaration)

        case EnumLikeDeclaration():
            yield from serialize_enum_like_declaration(declaration)

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


def serialize_class_like_declaration(
    declaration: ClassLikeDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case ClassDeclaration(identifier, specifiers):
            yield chain(serialize_specifiers(specifiers), ("class", identifier, ";"))

        case ClassDefinition(identifier, declaration_blocks, parents, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("class", identifier),
                serialize_class_parents(parents),
            )
            yield ("{",)
            for declaration_block in declaration_blocks:
                yield (serialize_class_access(declaration_block.access), ":")
                for inner_declaration in declaration_block.declarations:
                    yield from serialize_declaration(inner_declaration)
            yield ("}",)

        case FinalClassDefinition(identifier, declaration_blocks, parents, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("class", identifier, "final"),
                serialize_class_parents(parents),
            )
            yield ("{",)
            for declaration_block in declaration_blocks:
                yield (f"{serialize_class_access(declaration_block.access)}:",)
                for inner_declaration in declaration_block.declarations:
                    yield from serialize_declaration(inner_declaration)
            yield ("}",)

        case StructDeclaration(identifier, specifiers):
            yield chain(serialize_specifiers(specifiers), ("struct", identifier, ";"))

        case StructDefinition(identifier, declaration_blocks, parents, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("struct", identifier),
                serialize_class_parents(parents),
            )
            yield ("{",)
            for declaration_block in declaration_blocks:
                yield (f"{serialize_class_access(declaration_block.access)}:",)
                for inner_declaration in declaration_block.declarations:
                    yield from serialize_declaration(inner_declaration)
            yield ("}",)

        case FinalStructDefinition(identifier, declaration_blocks, parents, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("struct", identifier, "final"),
                serialize_class_parents(parents),
            )
            yield ("{",)
            for declaration_block in declaration_blocks:
                yield (f"{serialize_class_access(declaration_block.access)}:",)
                for inner_declaration in declaration_block.declarations:
                    yield from serialize_declaration(inner_declaration)
            yield ("}",)

        case _:
            raise TypeError(f"Unexpected type {type(declaration)}")


def serialize_class_parents(parents: list[ClassParent]) -> Iterable[str]:
    if len(parents) == 0:
        return

    yield ":"
    for parent in parents:
        if parent.virtual:
            yield "virtual"
        yield serialize_class_access(parent.access)
        yield parent.identifier


def serialize_enum_like_declaration(
    declaration: EnumLikeDeclaration,
) -> Iterable[Iterable[str]]:
    match declaration:
        case EnumDeclaration(identifier, specifiers):
            yield chain(serialize_specifiers(specifiers), ("enum", identifier, ";"))

        case EnumDefinition(identifier, members, specifiers):
            yield chain(serialize_specifiers(specifiers), ("enum", identifier))
            yield ("{",)
            for member in members:
                yield chain(
                    (member.identifier, "="),
                    serialize_expression(member.value),
                )
            yield ("}",)

        case ScopedEnumDeclaration(identifier, underlying_type, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("enum", "class", identifier),
                (":", underlying_type) if underlying_type is not None else (),
                (";",),
            )

        case ScopedEnumDefinition(identifier, underlying_type, members, specifiers):
            yield chain(
                serialize_specifiers(specifiers),
                ("enum", "class", identifier),
                (":", underlying_type) if underlying_type is not None else (),
            )
            yield ("{",)
            for member in members:
                yield chain(
                    (member.identifier, "="),
                    serialize_expression(member.value),
                )
            yield ("}",)


def serialize_specifiers(specifiers: Specifier) -> Iterable[str]:
    if Specifier.CONSTEXPR in specifiers:
        yield "constexpr"

    if Specifier.EXTERN in specifiers:
        yield "extern"

    if Specifier.EXTERN_C in specifiers:
        yield 'extern "C"'

    if Specifier.FRIEND in specifiers:
        yield "friend"

    if Specifier.INLINE in specifiers:
        yield "inline"

    if Specifier.MUTABLE in specifiers:
        yield "mutable"

    if Specifier.REGISTER in specifiers:
        yield "register"

    if Specifier.STATIC in specifiers:
        yield "static"

    if Specifier.THREAD_LOCAL in specifiers:
        yield "thread_local"


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
