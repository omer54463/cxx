from dataclasses import dataclass

from surgeon.expression.constant_expression import ConstantExpression
from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class CaseStatement(LabeledStatement):
    value: ConstantExpression
