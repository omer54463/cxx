from dataclasses import dataclass


@dataclass
class Expression:
    def __post_init__(self) -> None:
        if type(self) == Expression:
            raise TypeError("Don't use this class - use a subclass.")
