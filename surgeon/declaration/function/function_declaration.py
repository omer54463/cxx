from dataclasses import dataclass, field

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.function.function_argument import FunctionArgument
from surgeon.declaration.specifier import Specifier


@dataclass
class FunctionDeclaration(Declaration):
    return_type: str
    identifier: str
    arguments: list[FunctionArgument] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
