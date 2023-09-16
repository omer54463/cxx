from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class IfConstexprElseStatement(SelectionStatement):
    condition: Expression
    content: Statement
    else_content: Statement
    initialization: Statement | None = None
