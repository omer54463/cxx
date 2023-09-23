from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class IfElseStatement(SelectionStatement):
    condition: Expression
    content: Statement
    else_content: Statement
    initializer: Statement | None
    constexpr: bool
