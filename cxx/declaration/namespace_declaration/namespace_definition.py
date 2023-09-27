from dataclasses import dataclass

from cxx.declaration.declaration import Declaration
from cxx.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)


@dataclass
class NamespaceDefinition(NamespaceDeclaration):
    declarations: list[Declaration]
