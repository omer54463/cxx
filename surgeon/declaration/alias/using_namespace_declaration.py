from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class UsingNamespaceDeclaration(Declaration):
    identifier: str
