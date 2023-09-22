from dataclasses import dataclass


@dataclass
class Literal:
    def __post_init__(self) -> None:
        if type(self) == Literal:
            raise TypeError("Don't use this class - use a subclass.")
