from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.iteration_statement.iteration_statement import IterationStatement
from cxx.statement.statement import Statement


@dataclass
class WhileStatement(IterationStatement):
    condition: Expression
    content: Statement
