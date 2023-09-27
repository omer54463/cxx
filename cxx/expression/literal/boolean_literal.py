from dataclasses import dataclass

from cxx.expression.literal.literal import Literal


@dataclass
class BooleanLiteral(Literal):
    value: bool
