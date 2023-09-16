from dataclasses import dataclass

from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement
from surgeon.statement.statement import Statement


@dataclass
class GotoTargetStatement(LabeledStatement):
    name: str
    content: Statement
