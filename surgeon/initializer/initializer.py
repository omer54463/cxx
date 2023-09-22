from dataclasses import dataclass


@dataclass
class Initializer:
    def __post_init__(self) -> None:
        if type(self) == Initializer:
            raise TypeError("Don't use this class - use a subclass.")
