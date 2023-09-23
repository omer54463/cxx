from dataclasses import dataclass

from surgeon.declaration.enum.enum_like_declaration import EnumLikeDeclaration
from surgeon.declaration.specifier import Specifier


@dataclass
class EnumDeclaration(EnumLikeDeclaration):
    identifier: str
    specifiers: Specifier = Specifier.NONE
