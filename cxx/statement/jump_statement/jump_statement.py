from dataclasses import dataclass

from cxx.statement.statement import Statement


@dataclass
class JumpStatement(Statement):
    def __post_init__(self) -> None:
        if type(self) == JumpStatement:
            raise TypeError("Don't use this class - use a subclass.")
