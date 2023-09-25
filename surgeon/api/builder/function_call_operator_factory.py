from __future__ import annotations

from typing import TYPE_CHECKING

from surgeon.expression.operator.other_operators import FunctionCallOperator

if TYPE_CHECKING:
    from surgeon.expression.expression import Expression


class FunctionCallOperatorFactory:
    operand: Expression
    arguments: list[Expression]

    def __init__(self, operand: Expression) -> None:
        self.operand = operand
        self.arguments = []

    def add_argument(self, argument: Expression) -> FunctionCallOperatorFactory:
        self.arguments.append(argument)
        return self

    def build(self) -> FunctionCallOperator:
        return FunctionCallOperator(self.operand, self.arguments)
