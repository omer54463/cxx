from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class NamespaceDeclaration(Declaration):
    specificers: list[str]
    identifier: str
