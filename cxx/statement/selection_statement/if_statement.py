from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.selection_statement.selection_statement import SelectionStatement
from cxx.statement.statement import Statement


@dataclass
class IfStatement(SelectionStatement):
    constexpr: bool
    initializer: Statement | None
    condition: Expression
    content: Statement
    else_content: Statement | None
