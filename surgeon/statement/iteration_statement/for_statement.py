from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.iteration_statement.iteration_statement import IterationStatement
from surgeon.statement.statement import Statement


@dataclass
class ForStatement(IterationStatement):
    initialization: Statement
    content: Statement
    condition: Expression | None = None
    progression: Expression | None = None
