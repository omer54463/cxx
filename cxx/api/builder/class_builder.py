from __future__ import annotations

import typing as t
from dataclasses import dataclass

from cxx.declaration.class_declaration.class_base import ClassBase
from cxx.declaration.class_declaration.class_declaration import ClassDeclaration
from cxx.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from cxx.declaration.class_declaration.class_definition import ClassDefinition

if t.TYPE_CHECKING:
    from cxx.declaration.class_declaration.class_access import ClassAccess
    from cxx.declaration.declaration import Declaration


@dataclass
class Class:
    declaration: ClassDeclaration
    definition: ClassDefinition


class ClassBuilder:
    identifier: str
    struct: bool
    final: bool
    specifiers: list[str]
    bases: list[ClassBase]
    blocks: list[ClassDeclarationBlock]
    current_block: ClassDeclarationBlock

    def __init__(
        self,
        identifier: str,
        *,
        struct: bool = False,
        final: bool = False,
    ) -> None:
        self.identifier = identifier
        self.struct = struct
        self.final = final
        self.specifiers = []
        self.bases = []
        self.blocks = []
        self.current_block = ClassDeclarationBlock(access=None, declarations=[])

    def add_specifier(self, specifier: str) -> ClassBuilder:
        self.specifiers.append(specifier)
        return self

    def add_base(
        self,
        identifier: str,
        access: ClassAccess | None = None,
        *,
        virtual: bool = False,
    ) -> ClassBuilder:
        self.bases.append(ClassBase(virtual, access, identifier))
        return self

    def set_access(self, access: ClassAccess) -> ClassBuilder:
        self.blocks.append(self.current_block)
        self.current_block = ClassDeclarationBlock(access=access, declarations=[])
        return self

    def add_declaration(self, declaration: Declaration) -> ClassBuilder:
        self.current_block.declarations.append(declaration)
        return self

    def build(self) -> Class:
        return Class(
            ClassDeclaration(self.specifiers, self.struct, self.identifier),
            ClassDefinition(
                self.specifiers,
                self.struct,
                self.identifier,
                self.final,
                self.bases,
                [*self.blocks, self.current_block]
                if len(self.current_block.declarations) > 0
                else self.blocks,
            ),
        )
