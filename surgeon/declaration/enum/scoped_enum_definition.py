from dataclasses import dataclass, field

from surgeon.declaration.enum.enum_like_declaration import EnumLikeDeclaration
from surgeon.declaration.enum.enum_member import EnumMember
from surgeon.declaration.specifier import Specifier


@dataclass
class ScopedEnumDefinition(EnumLikeDeclaration):
    identifier: str
    underlying_type: str | None = None
    members: list[EnumMember] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
