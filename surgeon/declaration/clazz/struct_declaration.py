from dataclasses import dataclass

from surgeon.declaration.clazz.class_like_declaration import ClassLikeDeclaration
from surgeon.declaration.specifier import Specifier


@dataclass
class StructDeclaration(ClassLikeDeclaration):
    identifier: str
    specifiers: Specifier = Specifier.NONE
