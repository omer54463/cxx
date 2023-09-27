from dataclasses import dataclass

from cxx.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class LabelStatement(LabeledStatement):
    identifier: str
