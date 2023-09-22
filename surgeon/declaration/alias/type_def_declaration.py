from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class TypeDefDeclaration(Declaration):
    new_type: str
    old_type: str
