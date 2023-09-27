from dataclasses import dataclass

from cxx.statement.jump_statement.jump_statement import JumpStatement


@dataclass
class ContinueStatement(JumpStatement):
    pass
