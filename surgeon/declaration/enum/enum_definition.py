from dataclasses import dataclass, field

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum.enum_member import EnumMember
from surgeon.declaration.specifier import Specifier


@dataclass
class EnumDefinition(Declaration):
    identifier: str
    members: list[EnumMember] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
