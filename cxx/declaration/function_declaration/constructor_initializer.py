from dataclasses import dataclass

from cxx.expression.expression import Expression


@dataclass
class ConstructorInitializer:
    identifier: str
    value: Expression | None
