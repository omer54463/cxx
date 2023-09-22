from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier


@dataclass
class NamespaceDeclaration(Declaration):
    identifier: str
    specifiers: Specifier = Specifier.NONE
