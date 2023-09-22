from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class UsingEnumDeclaration(Declaration):
    identifier: str
