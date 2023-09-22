from dataclasses import dataclass

from surgeon.declaration.alias.alias_like_declaration import AliasLikeDeclaration


@dataclass
class UsingNamespaceDeclaration(AliasLikeDeclaration):
    identifier: str
