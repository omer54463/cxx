from dataclasses import dataclass

from surgeon.expression.expression import Expression


@dataclass
class ConstantExpression(Expression):
    pass
