from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier


@dataclass
class SimpleDeclaration(Declaration):
    type: str
    identifier: str
    specifiers: Specifier = Specifier.NONE
