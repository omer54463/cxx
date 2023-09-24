from dataclasses import dataclass

from surgeon.expression.literal.literal import Literal


@dataclass
class IdentifierLiteral(Literal):
    identifier: str
