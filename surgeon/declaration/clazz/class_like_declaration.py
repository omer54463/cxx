from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration


@dataclass
class ClassLikeDeclaration(Declaration):
    def __post_init__(self) -> None:
        if type(self) == ClassLikeDeclaration:
            raise TypeError("Don't use this class - use a subclass.")
