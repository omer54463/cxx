from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class AliasDeclaration(Declaration):
    new_type: str
    old_type: str
