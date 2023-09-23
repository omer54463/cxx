from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.function_declaration.function_argument import FunctionArgument


@dataclass
class FunctionDeclaration(Declaration):
    specifiers: list[str]
    return_type: str
    identifier: str
    arguments: list[FunctionArgument]
