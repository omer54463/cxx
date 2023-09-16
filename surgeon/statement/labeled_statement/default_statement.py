from dataclasses import dataclass

from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement


@dataclass
class DefaultStatement(LabeledStatement):
    pass
