from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class CaseStatement(LabeledStatement):
    value: Expression
