from surgeon.builder.class_builder import ClassBuilder
from surgeon.declaration.class_declaration.class_access import ClassAccess
from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from surgeon.declaration.class_declaration.class_definition import ClassDefinition
from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration


class TestClassBuilder:
    def test_simple(self) -> None:
        result = ClassBuilder("identifier").build()
        expected_declaration = ClassDeclaration([], False, "identifier")
        expected_definition = ClassDefinition([], False, "identifier", False, [], [])

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition

    def test_complex(self) -> None:
        result = (
            ClassBuilder("identifier", struct=True, final=True)
            .add_specifier("specifier")
            .add_base("identifier", ClassAccess.PUBLIC, virtual=True)
            .add_declaration(SimpleDeclaration([], "type", "identifier"))
            .set_access(ClassAccess.PRIVATE)
            .add_declaration(SimpleDeclaration([], "type", "identifier"))
            .build()
        )
        expected_declaration = ClassDeclaration(["specifier"], True, "identifier")
        expected_definition = ClassDefinition(
            ["specifier"],
            True,
            "identifier",
            True,
            [
                ClassBase(True, ClassAccess.PUBLIC, "identifier"),
            ],
            [
                ClassDeclarationBlock(
                    None,
                    [SimpleDeclaration([], "type", "identifier")],
                ),
                ClassDeclarationBlock(
                    ClassAccess.PRIVATE,
                    [SimpleDeclaration([], "type", "identifier")],
                ),
            ],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition
