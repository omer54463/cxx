from enum import Flag, auto


class Specifier(Flag):
    NONE = 0
    CONSTEXPR = auto()
    EXTERN = auto()
    EXTERN_C = auto()
    FRIEND = auto()
    INLINE = auto()
    MUTABLE = auto()
    REGISTER = auto()
    STATIC = auto()
    THREAD_LOCAL = auto()
