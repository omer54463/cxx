from dataclasses import dataclass

from surgeon.statement.statement import Statement


@dataclass
class NullStatement(Statement):
    pass
