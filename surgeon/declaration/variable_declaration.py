from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.expression.expression import Expression


@dataclass
class SimpleDeclaration(Declaration):
    specifiers: list[str]
    type: str
    identifier: str
    value: Expression | None
