from dataclasses import dataclass

from cxx.expression.literal.literal import Literal


@dataclass
class IdentifierLiteral(Literal):
    identifier: str
