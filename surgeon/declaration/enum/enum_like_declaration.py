from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class EnumLikeDeclaration(Declaration):
    def __post_init__(self) -> None:
        if type(self) == EnumLikeDeclaration:
            raise TypeError("Don't use this class - use a subclass.")
