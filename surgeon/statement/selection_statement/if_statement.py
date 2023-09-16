from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class IfEntry:
    condition: Expression
    statement: Statement


@dataclass
class IfStatement(SelectionStatement):
    if_entry: IfEntry
    else_if_entries: list[IfEntry]
    else_statement: Statement | None
