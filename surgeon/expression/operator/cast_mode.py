from enum import Enum, auto


class CastMode(Enum):
    CLASSIC = auto()
    STATIC = auto()
    DYNAMIC = auto()
    CONST = auto()
    REINTERPRET = auto()
