from dataclasses import dataclass

from surgeon.expression.constant_expression import ConstantExpression
from surgeon.expression.expression import Expression
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.statement import Statement


@dataclass
class SwitchEntry:
    value: ConstantExpression
    statement: Statement


@dataclass
class SwitchStatement(SelectionStatement):
    expression: Expression
    cases: list[SwitchEntry]
