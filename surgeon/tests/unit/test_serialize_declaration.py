from collections.abc import Iterable
from itertools import chain

import pytest

from surgeon.declaration.class_declaration.class_access import ClassAccess
from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from surgeon.declaration.class_declaration.class_definition import ClassDefinition
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum_declaration.enum_declaration import EnumDeclaration
from surgeon.declaration.enum_declaration.enum_definition import EnumDefinition
from surgeon.declaration.enum_declaration.enum_member import EnumMember
from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from surgeon.declaration.simple_declaration.simple_definition import SimpleDefinition
from surgeon.declaration.static_assert_declaration import StaticAssertDeclaration
from surgeon.serialize.serialize_declaration import serialize_declaration
from surgeon.tests.unit.mocks.mock_serialize_expression import FakeExpression
from surgeon.tests.unit.mocks.mock_serialize_literal import FakeLiteral

BASIC_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        StaticAssertDeclaration(FakeExpression("expression"), FakeLiteral("literal")),
        [
            ["static_assert", "(", "expression", "literal", ")", ";"],
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
                        SimpleDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
                        ),
                    ],
                ),
                ClassDeclarationBlock(
                    access=ClassAccess.PROTECTED,
                    declarations=[
                        SimpleDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
                        ),
                    ],
                ),
                ClassDeclarationBlock(
                    access=ClassAccess.PRIVATE,
                    declarations=[
                        SimpleDeclaration(
                            specifiers=[],
                            type="type",
                            identifier="identifier",
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
        ),
        [
            ["enum", "identifier", ";"],
        ],
    ),
    (
        EnumDeclaration(
            specifiers=["specifier"],
            scoped=False,
            identifier="identifier",
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
            members=[],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["}"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=["specifier"],
            scoped=False,
            identifier="identifier",
            members=[],
        ),
        [
            ["specifier", "enum", "identifier"],
            ["{"],
            ["}"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=["specifier"],
            scoped=True,
            identifier="identifier",
            members=[],
        ),
        [
            ["specifier", "enum", "class", "identifier"],
            ["{"],
            ["}"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            members=[EnumMember(identifier="member", value=None)],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["member", ","],
            ["}"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
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
            ["}"],
        ],
    ),
    (
        EnumDefinition(
            specifiers=[],
            scoped=False,
            identifier="identifier",
            members=[
                EnumMember(identifier="member", value=FakeExpression("expression")),
            ],
        ),
        [
            ["enum", "identifier"],
            ["{"],
            ["member", "=", "expression", ","],
            ["}"],
        ],
    ),
)

SIMPLE_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        SimpleDeclaration(
            specifiers=[],
            type="type",
            identifier="identifier",
        ),
        [
            ["type", "identifier", ";"],
        ],
    ),
    (
        SimpleDeclaration(
            specifiers=["specifier"],
            type="type",
            identifier="identifier",
        ),
        [
            ["specifier", "type", "identifier", ";"],
        ],
    ),
    (
        SimpleDefinition(
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
        SimpleDefinition(
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

DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = chain(
    BASIC_DECLARATION_TEST_DATA,
    CLASS_DECLARATION_TEST_DATA,
    ENUM_DECLARATION_TEST_DATA,
    SIMPLE_DECLARATION_TEST_DATA,
)


@pytest.mark.usefixtures("mock_serialize_expression", "mock_serialize_literal")
@pytest.mark.parametrize(("declaration", "expected"), DECLARATION_TEST_DATA)
def test_serialize_declaration(
    declaration: Declaration,
    expected: list[list[str]],
) -> None:
    declaration_lines = serialize_declaration(declaration)
    declaration_lines_as_lists = [list(line) for line in declaration_lines]

    assert declaration_lines_as_lists == expected
