from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class EnumDeclaration(Declaration):
    specifiers: list[str]
    scoped: bool
    identifier: str
