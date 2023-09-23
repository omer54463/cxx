from dataclasses import dataclass

from surgeon.declaration.alias_declaration.alias_mode import AliasMode
from surgeon.declaration.declaration import Declaration


@dataclass
class AliasDeclaration(Declaration):
    mode: AliasMode
    old_identifier: str
    new_identifier: str
