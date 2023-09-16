from dataclasses import dataclass

from surgeon.expression.raw_expression import RawExpression
from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class CaseStatement(LabeledStatement):
    value: RawExpression
