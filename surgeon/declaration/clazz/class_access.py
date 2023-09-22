from enum import Flag, auto


class ClassAccess(Flag):
    NONE = 0
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()
