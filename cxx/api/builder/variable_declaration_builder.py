from __future__ import annotations

from typing import TYPE_CHECKING

from cxx.declaration.simple_declaration.variable_declaration import (
    VariableDeclaration,
)

if TYPE_CHECKING:
    from cxx.expression.expression import Expression


class VariableDeclarationBuilder:
    type: str
    identifier: str
    value: Expression | None
    specifiers: list[str]

    def __init__(
        self,
        type: str,
        identifier: str,
        value: Expression | None = None,
    ) -> None:
        self.type = type
        self.identifier = identifier
        self.value = value
        self.specifiers = []

    def add_specifier(self, specifier: str) -> VariableDeclarationBuilder:
        self.specifiers.append(specifier)
        return self

    def build(self) -> VariableDeclaration:
        return VariableDeclaration(
            self.specifiers,
            self.type,
            self.identifier,
            self.value,
        )
