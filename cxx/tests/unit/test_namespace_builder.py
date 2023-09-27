from cxx.api.builder.namespace_builder import NamespaceBuilder
from cxx.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)
from cxx.declaration.namespace_declaration.namespace_definition import (
    NamespaceDefinition,
)
from cxx.declaration.simple_declaration.variable_declaration import (
    VariableDeclaration,
)


class TestNamespaceBuilder:
    def test_simple(self) -> None:
        result = NamespaceBuilder("identifier").build()
        expected_declaration = NamespaceDeclaration([], "identifier")
        expected_definition = NamespaceDefinition([], "identifier", [])

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition

    def test_complex(self) -> None:
        result = (
            NamespaceBuilder("identifier")
            .add_specifier("specifier")
            .add_declaration(VariableDeclaration([], "type", "identifier", None))
            .build()
        )
        expected_declaration = NamespaceDeclaration(["specifier"], "identifier")
        expected_definition = NamespaceDefinition(
            ["specifier"],
            "identifier",
            [VariableDeclaration([], "type", "identifier", None)],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition
