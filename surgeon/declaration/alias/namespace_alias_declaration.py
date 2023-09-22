from dataclasses import dataclass

from surgeon.declaration.alias.alias_like_declaration import AliasLikeDeclaration


@dataclass
class NamespaceAliasDeclaration(AliasLikeDeclaration):
    new_identifier: str
    old_identifier: str
