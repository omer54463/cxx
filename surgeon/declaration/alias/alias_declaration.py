from dataclasses import dataclass

from surgeon.declaration.alias.alias_like_declaration import AliasLikeDeclaration


@dataclass
class AliasDeclaration(AliasLikeDeclaration):
    new_type: str
    old_type: str
