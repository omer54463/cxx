from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier


@dataclass
class EnumDeclaration(Declaration):
    name: str
    specifiers: Specifier = Specifier.NONE
