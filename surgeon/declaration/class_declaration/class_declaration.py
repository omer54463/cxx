from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class ClassDeclaration(Declaration):
    specifiers: list[str]
    struct: bool
    identifier: str
