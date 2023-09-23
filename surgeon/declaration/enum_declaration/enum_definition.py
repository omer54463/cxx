from dataclasses import dataclass

from surgeon.declaration.enum_declaration.enum_declaration import EnumDeclaration
from surgeon.declaration.enum_declaration.enum_member import EnumMember


@dataclass
class EnumDefinition(EnumDeclaration):
    members: list[EnumMember]
