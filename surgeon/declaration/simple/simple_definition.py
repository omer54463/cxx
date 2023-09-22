from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier
from surgeon.initializer.initializer import Initializer


@dataclass
class SimpleDeclaration(Declaration):
    type: str
    identifier: str
    initializer: Initializer
    specifiers: Specifier = Specifier.NONE
