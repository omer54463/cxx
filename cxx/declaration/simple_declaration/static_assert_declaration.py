from dataclasses import dataclass

from cxx.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from cxx.expression.expression import Expression


@dataclass
class StaticAssertDeclaration(SimpleDeclaration):
    expression: Expression
    message: Expression
