from dataclasses import dataclass

from cxx.expression.expression import Expression


@dataclass
class Operator(Expression):
    def __post_init__(self) -> None:
        if type(self) == Operator:
            raise TypeError("Don't use this class - use a subclass.")


@dataclass
class UnaryOperator(Operator):
    operand: Expression


@dataclass
class BinaryOperator(Operator):
    left_operand: Expression
    right_operand: Expression


@dataclass
class TrinaryOperator(Operator):
    left_operand: Expression
    middle_operand: Expression
    right_operand: Expression
