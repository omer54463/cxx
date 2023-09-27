from cxx.api.builder.class_builder import ClassBuilder
from cxx.declaration.class_declaration.class_access import ClassAccess
from cxx.declaration.class_declaration.class_base import ClassBase
from cxx.declaration.class_declaration.class_declaration import ClassDeclaration
from cxx.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from cxx.declaration.class_declaration.class_definition import ClassDefinition
from cxx.declaration.simple_declaration.variable_declaration import (
    VariableDeclaration,
)


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
            .add_declaration(VariableDeclaration([], "type", "identifier", None))
            .set_access(ClassAccess.PRIVATE)
            .add_declaration(VariableDeclaration([], "type", "identifier", None))
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
                    [VariableDeclaration([], "type", "identifier", None)],
                ),
                ClassDeclarationBlock(
                    ClassAccess.PRIVATE,
                    [VariableDeclaration([], "type", "identifier", None)],
                ),
            ],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition
