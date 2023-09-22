from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class UsingDeclaration(Declaration):
    identifier: str
