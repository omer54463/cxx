from dataclasses import dataclass

from surgeon.expression.literal.literal import Literal


@dataclass
class CharacterLiteral(Literal):
    value: str
