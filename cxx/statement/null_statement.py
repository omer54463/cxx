from dataclasses import dataclass

from cxx.statement.statement import Statement


@dataclass
class NullStatement(Statement):
    pass
