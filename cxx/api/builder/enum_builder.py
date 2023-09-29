from __future__ import annotations

import typing as t
from dataclasses import dataclass

from cxx.declaration.enum_declaration.enum_declaration import EnumDeclaration
from cxx.declaration.enum_declaration.enum_definition import EnumDefinition
from cxx.declaration.enum_declaration.enum_member import EnumMember

if t.TYPE_CHECKING:
    from cxx.expression.expression import Expression


@dataclass
class Enum:
    declaration: EnumDeclaration
    definition: EnumDefinition


class EnumBuilder:
    identifier: str
    scoped: bool
    underlying_type: str | None
    specifiers: list[str]
    members: list[EnumMember]

    def __init__(
        self,
        identifier: str,
        scoped: bool = False,
        underlying_type: str | None = None,
    ) -> None:
        self.identifier = identifier
        self.scoped = scoped
        self.underlying_type = underlying_type
        self.specifiers = []
        self.members = []

    def add_specifier(self, specifier: str) -> EnumBuilder:
        self.specifiers.append(specifier)
        return self

    def add_member(
        self,
        identifier: str,
        value: Expression | None = None,
    ) -> EnumBuilder:
        self.members.append(EnumMember(identifier, value))
        return self

    def build(self) -> Enum:
        return Enum(
            EnumDeclaration(
                self.specifiers,
                self.scoped,
                self.identifier,
                self.underlying_type,
            ),
            EnumDefinition(
                self.specifiers,
                self.scoped,
                self.identifier,
                self.underlying_type,
                self.members,
            ),
        )
