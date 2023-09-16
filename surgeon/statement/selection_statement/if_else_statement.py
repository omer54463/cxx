from ast import Expression
from dataclasses import dataclass

from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class IfElseStatement(SelectionStatement):
    condition: Expression
    then_statement: Statement
    else_statement: Statement
