from dataclasses import dataclass

from surgeon.statement.jump_statement.jump_statement import JumpStatement


@dataclass
class BreakStatement(JumpStatement):
    pass
