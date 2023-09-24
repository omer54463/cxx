from dataclasses import dataclass

from surgeon.expression.literal.literal import Literal


@dataclass
class StringLiteral(Literal):
    value: str
