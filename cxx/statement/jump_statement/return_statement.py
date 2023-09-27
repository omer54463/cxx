from dataclasses import dataclass

from cxx.expression.expression import Expression
from cxx.statement.jump_statement.jump_statement import JumpStatement


@dataclass
class ReturnStatement(JumpStatement):
    value: Expression | None
