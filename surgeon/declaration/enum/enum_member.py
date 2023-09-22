from dataclasses import dataclass

from surgeon.expression.expression import Expression


@dataclass
class EnumMember:
    identifier: str
    value: Expression
