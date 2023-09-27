from dataclasses import dataclass
from enum import Enum, auto

from cxx.expression.expression import Expression
from cxx.expression.operator.operator import (
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


class CastMode(Enum):
    STATIC = auto()
    DYNAMIC = auto()
    CONST = auto()
    REINTERPRET = auto()


@dataclass
class CastOperator(Operator):
    mode: CastMode
    type: str
    operand: Expression
