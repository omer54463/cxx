from dataclasses import dataclass

from surgeon.expression.constant_expression import ConstantExpression
from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement
from surgeon.statement.statement import Statement


@dataclass
class CaseStatement(LabeledStatement):
    value: ConstantExpression
    content: Statement
