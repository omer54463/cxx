from dataclasses import dataclass


@dataclass
class Declaration:
    def __post_init__(self) -> None:
        if type(self) == Declaration:
            raise TypeError("Don't use this class - use a subclass.")
