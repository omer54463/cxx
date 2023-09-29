from cxx.api.builder.enum_builder import EnumBuilder
from cxx.declaration.enum_declaration.enum_declaration import EnumDeclaration
from cxx.declaration.enum_declaration.enum_definition import EnumDefinition
from cxx.declaration.enum_declaration.enum_member import EnumMember
from cxx.expression.literal.identifier_literal import IdentifierLiteral


class TestEnumBuilder:
    def test_simple(self) -> None:
        result = EnumBuilder("identifier").build()
        expected_declaration = EnumDeclaration([], False, "identifier", None)
        expected_definition = EnumDefinition([], False, "identifier", None, [])

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition

    def test_complex(self) -> None:
        result = (
            EnumBuilder("identifier")
            .add_specifier("specifier")
            .add_member("identifier", IdentifierLiteral("value"))
            .build()
        )
        expected_declaration = EnumDeclaration(["specifier"], False, "identifier", None)
        expected_definition = EnumDefinition(
            ["specifier"],
            False,
            "identifier",
            None,
            [EnumMember("identifier", IdentifierLiteral("value"))],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition
