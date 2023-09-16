from dataclasses import dataclass

from surgeon.statement.statement import Statement


@dataclass
class CompountStatement(Statement):
    content: list[Statement]
