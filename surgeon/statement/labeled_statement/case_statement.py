from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class CaseStatement(LabeledStatement):
    value: Expression
