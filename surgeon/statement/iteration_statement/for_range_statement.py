from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.expression.expression import Expression
from surgeon.statement.iteration_statement.iteration_statement import IterationStatement
from surgeon.statement.statement import Statement


@dataclass
class ForRangeStatement(IterationStatement):
    value: Declaration
    range: Expression
    content: Statement
    initialization: Statement | None = None
