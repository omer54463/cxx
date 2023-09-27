from dataclasses import dataclass

from cxx.declaration.function_declaration.constructor_initializer import (
    ConstructorInitializer,
)
from cxx.declaration.function_declaration.function_declaration import (
    FunctionDeclaration,
)
from cxx.statement.statement import Statement


@dataclass
class FunctionDefinition(FunctionDeclaration):
    initializers: list[ConstructorInitializer]
    statements: list[Statement]
