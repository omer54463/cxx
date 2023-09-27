from dataclasses import dataclass

from cxx.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from cxx.expression.expression import Expression


@dataclass
class VariableDeclaration(SimpleDeclaration):
    specifiers: list[str]
    type: str
    identifier: str
    value: Expression | None
