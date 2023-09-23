from dataclasses import dataclass

from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)


@dataclass
class ClassDefinition(ClassDeclaration):
    final: bool
    bases: list[ClassBase]
    declaration_blocks: list[ClassDeclarationBlock]
