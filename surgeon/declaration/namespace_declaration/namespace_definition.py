from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)


@dataclass
class NamespaceDefinition(NamespaceDeclaration):
    declarations: list[Declaration]
