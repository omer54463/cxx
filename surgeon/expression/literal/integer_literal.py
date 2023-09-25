from dataclasses import dataclass
from enum import Enum, auto

from surgeon.expression.literal.literal import Literal


class IntegerBase(Enum):
    BINARY = auto()
    OCTAL = auto()
    DECIMAL = auto()
    HEXADECIMAL = auto()


@dataclass
class IntegerLiteral(Literal):
    value: int
    base: IntegerBase
