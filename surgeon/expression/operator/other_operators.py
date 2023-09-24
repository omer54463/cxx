from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.expression.operator.cast_mode import CastMode
from surgeon.expression.operator.operator import (
    BinaryOperator,
    Operator,
    TrinaryOperator,
)


@dataclass
class FunctionCallOperator(Operator):
    operand: Expression
    argument_operands: list[Expression]


@dataclass
class CommaOperator(BinaryOperator):
    pass


@dataclass
class ConditionalOperator(TrinaryOperator):
    pass


@dataclass
class CCastOperator(Operator):
    type: str
    operand: Expression


@dataclass
class CastOperator(Operator):
    type: str
    operand: Expression
    mode: CastMode
