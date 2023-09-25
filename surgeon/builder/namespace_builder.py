from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from surgeon.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)
from surgeon.declaration.namespace_declaration.namespace_definition import (
    NamespaceDefinition,
)

if TYPE_CHECKING:
    from surgeon.declaration.declaration import Declaration


@dataclass
class Namespace:
    declaration: NamespaceDeclaration
    definition: NamespaceDefinition


class NamespaceBuilder:
    identifier: str
    specifiers: list[str]
    declarations: list[Declaration]

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        self.specifiers = []
        self.declarations = []

    def add_specifier(self, specifier: str) -> NamespaceBuilder:
        self.specifiers.append(specifier)
        return self

    def add_declaration(self, declaration: Declaration) -> NamespaceBuilder:
        self.declarations.append(declaration)
        return self

    def build(self) -> Namespace:
        return Namespace(
            NamespaceDeclaration(self.specifiers, self.identifier),
            NamespaceDefinition(self.specifiers, self.identifier, self.declarations),
        )
