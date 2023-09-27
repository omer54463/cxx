from dataclasses import dataclass

from cxx.statement.statement import Statement


@dataclass
class CompountStatement(Statement):
    content: list[Statement]
