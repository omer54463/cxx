from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.expression.expression import Expression


@dataclass
class StaticAssertDeclaration(Declaration):
    expression: Expression
    message: Expression
