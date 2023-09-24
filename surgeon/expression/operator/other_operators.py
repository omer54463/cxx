from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.expression.operator.operator import (
    BinaryOperator,
    Operator,
    TrinaryOperator,
    UnaryOperator,
)


@dataclass
class FunctionCallOperator(Operator):
    function_operand: Expression
    argument_operands: list[Expression]


@dataclass
class CommaOperator(BinaryOperator):
    pass


@dataclass
class ConditionalOperator(TrinaryOperator):
    pass


@dataclass
class SizeOfOperator(UnaryOperator):
    pass


@dataclass
class AlignOfOperator(UnaryOperator):
    pass


@dataclass
class TypeIdOperator(UnaryOperator):
    pass
