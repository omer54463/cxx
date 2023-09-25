from dataclasses import dataclass

from surgeon.declaration.simple_declaration.alias_mode import AliasMode
from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration


@dataclass
class AliasDeclaration(SimpleDeclaration):
    mode: AliasMode
    old_identifier: str
    new_identifier: str
