from enum import Flag, auto


class Specifier(Flag):
    NONE = 0
    INLINE = auto()
    FRIEND = auto()
    CONSTEXPR = auto()
    REGISTER = auto()
    STATIC = auto()
    THREAD_LOCAL = auto()
    EXTERN = auto()
    MUTABLE = auto()
    EXTERN_C = auto()
