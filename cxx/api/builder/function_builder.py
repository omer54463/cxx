from __future__ import annotations

import typing as t
from dataclasses import dataclass

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

if t.TYPE_CHECKING:
    from cxx.expression.expression import Expression
    from cxx.statement.statement import Statement


@dataclass
class Function:
    declaration: FunctionDeclaration
    definition: FunctionDefinition


class FunctionBuilder:
    identifier: str
    return_type: str
    specifiers: list[str]
    arguments: list[FunctionArgument]
    constructor_initializers: list[ConstructorInitializer]
    statement: list[Statement]

    def __init__(self, identifier: str, return_type: str) -> None:
        self.identifier = identifier
        self.return_type = return_type
        self.specifiers = []
        self.arguments = []
        self.constructor_initializers = []
        self.statement = []

    def add_specifier(self, specifier: str) -> FunctionBuilder:
        self.specifiers.append(specifier)
        return self

    def add_argument(
        self,
        type: str,
        identifier: str | None = None,
        default: Expression | None = None,
    ) -> FunctionBuilder:
        self.arguments.append(FunctionArgument(type, identifier, default))
        return self

    def add_constructor_initializer(
        self,
        identifier: str,
        value: Expression | None,
    ) -> FunctionBuilder:
        self.constructor_initializers.append(ConstructorInitializer(identifier, value))
        return self

    def add_statement(self, statement: Statement) -> FunctionBuilder:
        self.statement.append(statement)
        return self

    def build(self) -> Function:
        return Function(
            FunctionDeclaration(
                self.specifiers,
                self.return_type,
                self.identifier,
                self.arguments,
            ),
            FunctionDefinition(
                self.specifiers,
                self.return_type,
                self.identifier,
                self.arguments,
                self.constructor_initializers,
                self.statement,
            ),
        )
