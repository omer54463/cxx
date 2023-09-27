from dataclasses import dataclass

from cxx.expression.operator.operator import BinaryOperator, UnaryOperator


@dataclass
class NotOperator(UnaryOperator):
    pass


@dataclass
class AndOperator(BinaryOperator):
    pass


@dataclass
class OrOperator(BinaryOperator):
    pass
