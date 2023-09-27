from dataclasses import dataclass

from cxx.expression.expression import Expression


@dataclass
class EnumMember:
    identifier: str
    value: Expression | None
