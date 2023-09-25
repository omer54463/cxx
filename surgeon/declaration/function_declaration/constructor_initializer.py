from dataclasses import dataclass

from surgeon.expression.expression import Expression


@dataclass
class ConstructorInitializer:
    identifier: str
    value: Expression | None
