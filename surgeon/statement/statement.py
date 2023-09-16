from dataclasses import dataclass


@dataclass
class Statement:
    def __post_init__(self) -> None:
        if type(self) == Statement:
            msg = "Don't use this class - use a subclass."
            raise TypeError(msg)
