from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.expression.expression import Expression
from surgeon.literal.literal import Literal


@dataclass
class StaticAssertDeclaration(Declaration):
    expression: Expression
    literal: Literal
