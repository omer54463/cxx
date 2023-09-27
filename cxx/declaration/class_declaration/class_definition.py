from dataclasses import dataclass

from cxx.declaration.class_declaration.class_base import ClassBase
from cxx.declaration.class_declaration.class_declaration import ClassDeclaration
from cxx.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)


@dataclass
class ClassDefinition(ClassDeclaration):
    final: bool
    bases: list[ClassBase]
    declaration_blocks: list[ClassDeclarationBlock]
