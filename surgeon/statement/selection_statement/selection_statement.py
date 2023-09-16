from dataclasses import dataclass

from surgeon.statement.statement import Statement


@dataclass
class SelectionStatement(Statement):
    def __post_init__(self) -> None:
        if type(self) == SelectionStatement:
            msg = "Don't use this class - use a subclass."
            raise TypeError(msg)
