from collections.abc import Iterable
from itertools import chain

import pytest

from cxx.declaration.class_declaration.class_access import ClassAccess
from cxx.declaration.class_declaration.class_base import ClassBase
from cxx.declaration.class_declaration.class_declaration import ClassDeclaration
from cxx.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from cxx.declaration.class_declaration.class_definition import ClassDefinition
from cxx.declaration.declaration import Declaration
from cxx.declaration.enum_declaration.enum_declaration import EnumDeclaration
from cxx.declaration.enum_declaration.enum_definition import EnumDefinition
from cxx.declaration.enum_declaration.enum_member import EnumMember
from cxx.declaration.function_declaration.constructor_initializer import (
    ConstructorInitializer,
)
from cxx.declaration.function_declaration.function_argument import FunctionArgument
from cxx.declaration.function_declaration.function_declaration import (
    FunctionDeclaration,
)
from cxx.declaration.function_declaration.function_definition import (
    FunctionDefinition,
)
from cxx.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)
from cxx.declaration.namespace_declaration.namespace_definition import (
    NamespaceDefinition,
)
from cxx.declaration.simple_declaration.alias_declaration import (
    AliasDeclaration,
    AliasMode,
)
from cxx.declaration.simple_declaration.static_assert_declaration import (
    StaticAssertDeclaration,
)
from cxx.declaration.simple_declaration.using_declaration import (
    UsingDeclaration,
    UsingMode,
)
from cxx.declaration.simple_declaration.variable_declaration import (
    VariableDeclaration,
)
from cxx.serialize.serialize_declaration import serialize_declaration
from cxx.tests.unit.flatten_lines import flatten_lines
from cxx.tests.unit.mocks.mock_serialize_expression import FakeExpression
from cxx.tests.unit.mocks.mock_serialize_statement import FakeStatement

ALIAS_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        AliasDeclaration(
            mode=AliasMode.DEFAULT,
            old_identifier="old_identifier",
            new_identifier="new_identifier",
        ),
        [
            ["using", "new_identifier", "=", "old_identifier", ";"],
        ],
    ),
    (
        AliasDeclaration(
            mode=AliasMode.NAMESPACE,
            old_identifier="old_identifier",
            new_identifier="new_identifier",
        ),
        [
            ["namespace", "new_identifier", "=", "old_identifier", ";"],
        ],
    ),
    (
        AliasDeclaration(
            mode=AliasMode.TYPE_DEF,
            old_identifier="old_identifier",
            new_identifier="new_identifier",
        ),
        [
            ["typedef", "old_identifier", "new_identifier", ";"],
        ],
    ),
)

BASIC_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        StaticAssertDeclaration(
            expression=FakeExpression("expression"),
            message=FakeExpression("message"),
        ),
        [
            ["static_assert", "(", "expression", ",", "message", ")", ";"],
        ],
    ),
)

CLASS_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        ClassDeclaration(
            specifiers=[],
            struct=False,
            identifier="identifier",
        ),
        [
            ["class", "identifier", ";"],
        ],
    ),
    (
        ClassDeclaration(
            specifiers=[],
            struct=True,
            identifier="identifier",
        ),
        [
            ["struct", "identifier", ";"],
        ],
    ),
    (
        ClassDeclaration(
            specifiers=["specifier"],
            struct=False,
            identifier="identifier",
        ),
        [
            ["specifier", "class", "identifier", ";"],
        ],
    ),
    (
        ClassDefinition(
            specifiers=[],
            struct=False,
            identifier="identifier",
            final=False,
            bases=[],
            declaration_blocks=[],
        ),
        [
            ["class", "identifier"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        ClassDefinition(
            specifiers=[],
            struct=False,
            identifier="identifier",
            final=False,
            bases=[ClassBase(virtual=False, access=None, identifier="base")],
            declaration_blocks=[],
        ),
        [
            ["class", "identifier", ":", "base"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        ClassDefinition(
            specifiers=[],
            struct=False,
            identifier="identifier",
            final=True,
            bases=[ClassBase(virtual=False, access=None, identifier="base")],
            declaration_blocks=[],
        ),
        [
            ["class", "identifier", "final", ":", "base"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        ClassDefinition(
            specifiers=[],
            struct=False,
            identifier="identifier",
            final=False,
            bases=[
                ClassBase(virtual=False, access=None, identifier="base_1"),
                ClassBase(virtual=True, access=ClassAccess.PUBLIC, identifier="base_2"),
            ],
            declaration_blocks=[],
        ),
        [
            ["class", "identifier", ":", "base_1", "virtual", "public", "base_2"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        ClassDefinition(
            specifiers=[],
            struct=False,
            identifier="identifier",
            final=False,
            bases=[],
            declaration_blocks=[
                ClassDeclarationBlock(
                    access=ClassAccess.PUBLIC,
                    declarations=[
                        VariableDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
                            value=None,
                        ),
                    ],
                ),
                ClassDeclarationBlock(
                    access=ClassAccess.PROTECTED,
                    declarations=[
                        VariableDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
                            value=None,
                        ),
                    ],
                ),
                ClassDeclarationBlock(
                    access=ClassAccess.PRIVATE,
                    declarations=[
                        VariableDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
                            value=None,
                        ),
                    ],
                ),
            ],
        ),
        [
            ["class", "identifier"],
            ["{"],
            ["public", ":"],
            ["type", "identifier", ";"],
            ["protected", ":"],
            ["type", "identifier", ";"],
            ["private", ":"],
            ["type", "identifier", ";"],
            ["}", ";"],
        ],
    ),
)

ENUM_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        EnumDeclaration(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
        ),
        [
            ["enum", "identifier", ";"],
        ],
    ),
    (
        EnumDeclaration(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type="type",
        ),
        [
            ["enum", "identifier", ":", "type", ";"],
        ],
    ),
    (
        EnumDeclaration(
            specifiers=["specifier"],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
        ),
        [
            ["specifier", "enum", "identifier", ";"],
        ],
    ),
    (
        EnumDeclaration(
            specifiers=["specifier"],
            scoped=True,
            identifier="identifier",
            underlying_type=None,
        ),
        [
            ["specifier", "enum", "class", "identifier", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
            members=[],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type="type",
            members=[],
        ),
        [
            ["enum", "identifier", ":", "type"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=["specifier"],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
            members=[],
        ),
        [
            ["specifier", "enum", "identifier"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=["specifier"],
            scoped=True,
            identifier="identifier",
            underlying_type=None,
            members=[],
        ),
        [
            ["specifier", "enum", "class", "identifier"],
            ["{"],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
            members=[EnumMember(identifier="member", value=None)],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["member", ","],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
            members=[
                EnumMember(identifier="member_1", value=None),
                EnumMember(identifier="member_2", value=None),
            ],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["member_1", ","],
            ["member_2", ","],
            ["}", ";"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            underlying_type=None,
            members=[
                EnumMember(identifier="member", value=FakeExpression("expression")),
            ],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["member", "=", "expression", ","],
            ["}", ";"],
        ],
    ),
)

SIMPLE_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        VariableDeclaration(
            specifiers=[],
            type="type",
            identifier="identifier",
            value=None,
        ),
        [
            ["type", "identifier", ";"],
        ],
    ),
    (
        VariableDeclaration(
            specifiers=["specifier"],
            type="type",
            identifier="identifier",
            value=None,
        ),
        [
            ["specifier", "type", "identifier", ";"],
        ],
    ),
    (
        VariableDeclaration(
            specifiers=[],
            type="type",
            identifier="identifier",
            value=FakeExpression("initializer"),
        ),
        [
            ["type", "identifier", "=", "initializer", ";"],
        ],
    ),
    (
        VariableDeclaration(
            specifiers=["specifier"],
            type="type",
            identifier="identifier",
            value=FakeExpression("initializer"),
        ),
        [
            ["specifier", "type", "identifier", "=", "initializer", ";"],
        ],
    ),
)

FUNCTION_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        FunctionDeclaration(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[],
        ),
        [
            ["return_type", "identifier", "(", ")", ";"],
        ],
    ),
    (
        FunctionDeclaration(
            specifiers=["specifier"],
            return_type="return_type",
            identifier="identifier",
            arguments=[],
        ),
        [
            ["specifier", "return_type", "identifier", "(", ")", ";"],
        ],
    ),
    (
        FunctionDeclaration(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(type="type", identifier="identifier", default=None),
            ],
        ),
        [
            ["return_type", "identifier", "(", "type", "identifier", ")", ";"],
        ],
    ),
    (
        FunctionDeclaration(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=None,
                ),
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=None,
                ),
            ],
        ),
        [
            ["return_type", "identifier"],
            ["(", "type", "identifier", ",", "type", "identifier", ")", ";"],
        ],
    ),
    (
        FunctionDeclaration(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=FakeExpression("expression"),
                ),
            ],
        ),
        [
            ["return_type", "identifier"],
            ["(", "type", "identifier", "=", "expression", ")", ";"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[],
            initializers=[],
            statements=[FakeStatement("statement")],
        ),
        [
            ["return_type", "identifier", "(", ")"],
            ["{"],
            ["statement", ";"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=["specifier"],
            return_type="return_type",
            identifier="identifier",
            arguments=[],
            initializers=[],
            statements=[
                FakeStatement("statement"),
            ],
        ),
        [
            ["specifier", "return_type", "identifier", "(", ")"],
            ["{"],
            ["statement", ";"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(type="type", identifier="identifier", default=None),
            ],
            initializers=[],
            statements=[
                FakeStatement("statement"),
            ],
        ),
        [
            ["return_type", "identifier", "(", "type", "identifier", ")"],
            ["{"],
            ["statement", ";"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=None,
                ),
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=None,
                ),
            ],
            initializers=[],
            statements=[
                FakeStatement("statement"),
            ],
        ),
        [
            ["return_type", "identifier"],
            ["(", "type", "identifier", ",", "type", "identifier", ")"],
            ["{"],
            ["statement", ";"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[
                FunctionArgument(
                    type="type",
                    identifier="identifier",
                    default=FakeExpression("expression"),
                ),
            ],
            initializers=[],
            statements=[FakeStatement("statement")],
        ),
        [
            ["return_type", "identifier"],
            ["(", "type", "identifier", "=", "expression", ")"],
            ["{"],
            ["statement", ";"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="return_type",
            identifier="identifier",
            arguments=[],
            initializers=[ConstructorInitializer("i", FakeExpression("e"))],
            statements=[],
        ),
        [
            ["return_type", "identifier", "(", ")", ":", "i", "(", "e", ")"],
            ["{"],
            ["}"],
        ],
    ),
    (
        FunctionDefinition(
            specifiers=[],
            return_type="rt",
            identifier="i",
            arguments=[],
            initializers=[
                ConstructorInitializer("i", FakeExpression("e")),
                ConstructorInitializer("i", FakeExpression("e")),
            ],
            statements=[],
        ),
        [
            ["rt", "i", "(", ")", ":", "i", "(", "e", ")", ",", "i", "(", "e", ")"],
            ["{"],
            ["}"],
        ],
    ),
)

NAMESPACE_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        NamespaceDeclaration(
            specificers=[],
            identifier="identifier",
        ),
        [
            ["namespace", "identifier", ";"],
        ],
    ),
    (
        NamespaceDeclaration(
            specificers=["specifier"],
            identifier="identifier",
        ),
        [
            ["specifier", "namespace", "identifier", ";"],
        ],
    ),
    (
        NamespaceDefinition(
            specificers=[],
            identifier="identifier",
            declarations=[],
        ),
        [
            ["namespace", "identifier"],
            ["{"],
            ["}"],
        ],
    ),
    (
        NamespaceDefinition(
            specificers=["specifier"],
            identifier="identifier",
            declarations=[],
        ),
        [
            ["specifier", "namespace", "identifier"],
            ["{"],
            ["}"],
        ],
    ),
    (
        NamespaceDefinition(
            specificers=[],
            identifier="identifier",
            declarations=[
                VariableDeclaration(
                    specifiers=[],
                    type="type",
                    identifier="identifier",
                    value=None,
                ),
            ],
        ),
        [
            ["namespace", "identifier"],
            ["{"],
            ["type", "identifier", ";"],
            ["}"],
        ],
    ),
)

USING_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        UsingDeclaration(
            mode=UsingMode.DEFAULT,
            identifier="identifier",
        ),
        [
            ["using", "identifier", ";"],
        ],
    ),
    (
        UsingDeclaration(
            mode=UsingMode.ENUM,
            identifier="identifier",
        ),
        [
            ["using", "enum", "identifier", ";"],
        ],
    ),
    (
        UsingDeclaration(
            mode=UsingMode.NAMESPACE,
            identifier="identifier",
        ),
        [
            ["using", "namespace", "identifier", ";"],
        ],
    ),
)

DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = chain(
    ALIAS_DECLARATION_TEST_DATA,
    BASIC_DECLARATION_TEST_DATA,
    CLASS_DECLARATION_TEST_DATA,
    ENUM_DECLARATION_TEST_DATA,
    FUNCTION_DECLARATION_TEST_DATA,
    NAMESPACE_DECLARATION_TEST_DATA,
    SIMPLE_DECLARATION_TEST_DATA,
    USING_DECLARATION_TEST_DATA,
)


@pytest.mark.usefixtures("mock_serialize_expression", "mock_serialize_statement")
@pytest.mark.parametrize(("declaration", "expected_lines"), DECLARATION_TEST_DATA)
def test_serialize_declaration(
    declaration: Declaration,
    expected_lines: list[list[str]],
) -> None:
    result = list(serialize_declaration(declaration))
    expected = list(flatten_lines(expected_lines))

    assert result == expected
