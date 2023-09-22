from dataclasses import dataclass, field

from surgeon.declaration.clazz.class_declaration_block import ClassDeclarationBlock
from surgeon.declaration.clazz.class_like_declaration import ClassLikeDeclaration
from surgeon.declaration.clazz.class_parent import ClassParent
from surgeon.declaration.specifier import Specifier


@dataclass
class FinalStructDefinition(ClassLikeDeclaration):
    identifier: str
    declaration_blocks: list[ClassDeclarationBlock] = field(default_factory=list)
    parents: list[ClassParent] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
