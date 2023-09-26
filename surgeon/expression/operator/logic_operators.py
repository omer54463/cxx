from dataclasses import dataclass

from surgeon.expression.operator.operator import BinaryOperator, UnaryOperator


@dataclass
class NotOperator(UnaryOperator):
    pass


@dataclass
class AndOperator(BinaryOperator):
    pass


@dataclass
class OrOperator(BinaryOperator):
    pass
