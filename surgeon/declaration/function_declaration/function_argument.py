from dataclasses import dataclass

from surgeon.expression.expression import Expression


@dataclass
class FunctionArgument:
    type: str
    identifier: str | None
    default: Expression | None
