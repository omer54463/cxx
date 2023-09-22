from dataclasses import dataclass, field

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.function.constructor_initializer import ConstructorInitializer
from surgeon.declaration.function.function_argument import FunctionArgument
from surgeon.declaration.specifier import Specifier
from surgeon.statement.statement import Statement


@dataclass
class FunctionDefinition(Declaration):
    return_type: str
    identifier: str
    arguments: list[FunctionArgument] = field(default_factory=list)
    initializers: list[ConstructorInitializer] = field(default_factory=list)
    statements: list[Statement] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
