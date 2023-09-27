from dataclasses import dataclass

from cxx.declaration.declaration import Declaration


@dataclass
class SimpleDeclaration(Declaration):
    def __post_init__(self) -> None:
        if type(self) == SimpleDeclaration:
            raise TypeError("Don't use this class - use a subclass.")
