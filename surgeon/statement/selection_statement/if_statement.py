from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class IfStatement(SelectionStatement):
    constexpr: bool
    initializer: Statement | None
    condition: Expression
    content: Statement
