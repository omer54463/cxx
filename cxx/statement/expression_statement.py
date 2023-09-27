from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.statement import Statement


@dataclass
class ExpressionStatement(Statement):
    content: Expression
