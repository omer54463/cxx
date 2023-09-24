from dataclasses import dataclass

from surgeon.expression.literal.literal import Literal


@dataclass
class BooleanLiteral(Literal):
    value: bool
