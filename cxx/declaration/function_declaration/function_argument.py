from dataclasses import dataclass

from cxx.expression.expression import Expression


@dataclass
class FunctionArgument:
    type: str
    identifier: str | None
    default: Expression | None
