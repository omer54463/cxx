from dataclasses import dataclass

from cxx.declaration.declaration import Declaration


@dataclass
class NamespaceDeclaration(Declaration):
    specificers: list[str]
    identifier: str
