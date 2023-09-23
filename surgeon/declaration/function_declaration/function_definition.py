from dataclasses import dataclass

from surgeon.declaration.function_declaration.constructor_initializer import (
    ConstructorInitializer,
)
from surgeon.declaration.function_declaration.function_declaration import (
    FunctionDeclaration,
)
from surgeon.statement.statement import Statement


@dataclass
class FunctionDefinition(FunctionDeclaration):
    initializers: list[ConstructorInitializer]
    statements: list[Statement]
