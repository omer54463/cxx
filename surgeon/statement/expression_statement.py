from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.statement import Statement


@dataclass
class CompountStatement(Statement):
    expression: Expression
