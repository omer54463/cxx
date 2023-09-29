from dataclasses import dataclass

from cxx.expression.literal.literal import Literal


@dataclass
class StringLiteral(Literal):
    value: str
    wide: bool
