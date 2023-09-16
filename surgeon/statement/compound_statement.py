from dataclasses import dataclass, field

from surgeon.statement.statement import Statement


@dataclass
class CompountStatement(Statement):
    content: list[Statement] = field(default_factory=list)
