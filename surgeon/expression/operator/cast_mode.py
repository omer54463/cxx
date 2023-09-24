from enum import Enum, auto


class CastMode(Enum):
    STATIC = auto()
    DYNAMIC = auto()
    CONST = auto()
    REINTERPRET = auto()
