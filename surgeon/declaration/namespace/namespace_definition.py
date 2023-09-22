from dataclasses import dataclass, field

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier


@dataclass
class NamespaceDefinition(Declaration):
    identifier: str
    declarations: list[Declaration] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
