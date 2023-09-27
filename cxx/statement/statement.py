from dataclasses import dataclass


@dataclass
class Statement:
    def __post_init__(self) -> None:
        if type(self) == Statement:
            raise TypeError("Don't use this class - use a subclass.")
