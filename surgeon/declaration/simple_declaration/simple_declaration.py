from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class SimpleDeclaration(Declaration):
    specifiers: list[str]
    type: str
    identifier: str
