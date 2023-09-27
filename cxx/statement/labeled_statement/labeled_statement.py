from dataclasses import dataclass

from cxx.statement.statement import Statement


@dataclass
class LabeledStatement(Statement):
    def __post_init__(self) -> None:
        if type(self) == LabeledStatement:
            raise TypeError("Don't use this class - use a subclass.")
