from dataclasses import dataclass

from cxx.declaration.declaration import Declaration
from cxx.statement.statement import Statement


@dataclass
class DeclarationStatement(Statement):
    content: Declaration
