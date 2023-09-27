from cxx.api.builder.function_builder import FunctionBuilder
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
from cxx.expression.literal.identifier_literal import IdentifierLiteral
from cxx.statement.null_statement import NullStatement


class TestFunctionBuilder:
    def test_simple(self) -> None:
        result = FunctionBuilder("identifier", "return_type").build()
        expected_declaration = FunctionDeclaration([], "return_type", "identifier", [])
        expected_definition = FunctionDefinition(
            [],
            "return_type",
            "identifier",
            [],
            [],
            [],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition

    def test_complex(self) -> None:
        result = (
            FunctionBuilder("identifier", "return_type")
            .add_specifier("specifier")
            .add_argument("type", "identifier", IdentifierLiteral("default"))
            .add_constructor_initializer("identifier", IdentifierLiteral("value"))
            .add_statement(NullStatement())
            .build()
        )
        expected_declaration = FunctionDeclaration(
            ["specifier"],
            "return_type",
            "identifier",
            [FunctionArgument("type", "identifier", IdentifierLiteral("default"))],
        )
        expected_definition = FunctionDefinition(
            ["specifier"],
            "return_type",
            "identifier",
            [FunctionArgument("type", "identifier", IdentifierLiteral("default"))],
            [ConstructorInitializer("identifier", IdentifierLiteral("value"))],
            [NullStatement()],
        )

        assert result.declaration == expected_declaration
        assert result.definition == expected_definition
