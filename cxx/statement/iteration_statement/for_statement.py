from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.iteration_statement.iteration_statement import IterationStatement
from cxx.statement.statement import Statement


@dataclass
class ForStatement(IterationStatement):
    initializer: Statement
    condition: Expression | None
    progression: Expression | None
    content: Statement
