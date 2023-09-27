from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.selection_statement.selection_statement import SelectionStatement
from cxx.statement.statement import Statement


@dataclass
class SwitchStatement(SelectionStatement):
    initializer: Statement | None
    value: Expression
    content: Statement
