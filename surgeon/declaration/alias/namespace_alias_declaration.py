from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class NamespaceAliasDeclaration(Declaration):
    new_identifier: str
    old_identifier: str
