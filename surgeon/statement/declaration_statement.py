from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.statement.statement import Statement


@dataclass
class DeclarationStatement(Statement):
    content: Declaration
