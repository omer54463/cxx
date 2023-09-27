from dataclasses import dataclass

from cxx.expression.literal.literal import Literal


@dataclass
class CharacterLiteral(Literal):
    value: str
