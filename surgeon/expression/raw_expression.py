from dataclasses import dataclass

from surgeon.expression.expression import Expression


@dataclass
class RawExpression(Expression):
    content: str
