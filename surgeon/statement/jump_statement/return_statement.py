from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.statement.jump_statement.jump_statement import JumpStatement


@dataclass
class ReturnStatement(JumpStatement):
    value: Expression
