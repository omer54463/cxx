from dataclasses import dataclass

from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from surgeon.expression.expression import Expression


@dataclass
class SimpleDefinition(SimpleDeclaration):
    value: Expression
