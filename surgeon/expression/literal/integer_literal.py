from dataclasses import dataclass

from surgeon.expression.literal.integer_base import IntegerBase
from surgeon.expression.literal.literal import Literal


@dataclass
class IntegerLiteral(Literal):
    value: int
    base: IntegerBase
