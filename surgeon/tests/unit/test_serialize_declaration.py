from collections.abc import Iterable
from itertools import chain

import pytest

from surgeon.declaration.alias.alias_declaration import AliasDeclaration
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
from surgeon.serialize.serialize_declaration import serialize_declaration
from surgeon.tests.unit.mocks.mock_serialize_expression import FakeExpression
from surgeon.tests.unit.mocks.mock_serialize_literal import FakeLiteral

BASIC_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        StaticAssertDeclaration(FakeExpression("expression"), FakeLiteral("literal")),
        [["static_assert", "(", "expression", "literal", ")", ";"]],
    ),
)

ALIAS_DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = (
    (
        AliasDeclaration("new_type", "old_type"),
        [["using", "new_type", "=", "old_type", ";"]],
    ),
    (
        NamespaceAliasDeclaration("new_identifier", "old_identifier"),
        [["namespace", "new_identifier", "=", "old_identifier", ";"]],
    ),
    (
        UsingDeclaration("identifier"),
        [["using", "identifier", ";"]],
    ),
    (
        UsingEnumDeclaration("identifier"),
        [["using", "enum", "identifier", ";"]],
    ),
    (
        UsingNamespaceDeclaration("identifier"),
        [["using", "namespace", "identifier", ";"]],
    ),
    (
        TypeDefDeclaration("new_type", "old_type"),
        [["typedef", "old_type", "new_type", ";"]],
    ),
)

DECLARATION_TEST_DATA: Iterable[tuple[Declaration, list[list[str]]]] = chain(
    BASIC_DECLARATION_TEST_DATA,
    ALIAS_DECLARATION_TEST_DATA,
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
