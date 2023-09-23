from dataclasses import dataclass

from surgeon.declaration.enum.enum_like_declaration import EnumLikeDeclaration
from surgeon.declaration.specifier import Specifier


@dataclass
class ScopedEnumDeclaration(EnumLikeDeclaration):
    identifier: str
    underlying_type: str | None = None
    specifiers: Specifier = Specifier.NONE
