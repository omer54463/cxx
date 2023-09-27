from dataclasses import dataclass

from cxx.declaration.enum_declaration.enum_declaration import EnumDeclaration
from cxx.declaration.enum_declaration.enum_member import EnumMember


@dataclass
class EnumDefinition(EnumDeclaration):
    members: list[EnumMember]
