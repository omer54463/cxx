from dataclasses import dataclass

from cxx.expression.operator.operator import BinaryOperator, UnaryOperator


@dataclass
class PlusOperator(UnaryOperator):
    pass


@dataclass
class MinusOperator(UnaryOperator):
    pass


@dataclass
class AdditionOperator(BinaryOperator):
    pass


@dataclass
class SubtractionOperator(BinaryOperator):
    pass


@dataclass
class MultiplicationOperator(BinaryOperator):
    pass


@dataclass
class DivisionOperator(BinaryOperator):
    pass


@dataclass
class RemainderOperator(BinaryOperator):
    pass


@dataclass
class BinaryNotOperator(UnaryOperator):
    pass


@dataclass
class BinaryAndOperator(BinaryOperator):
    pass


@dataclass
class BinaryOrOperator(BinaryOperator):
    pass


@dataclass
class BinaryXorOperator(BinaryOperator):
    pass


@dataclass
class LeftShiftOperator(BinaryOperator):
    pass


@dataclass
class RightShiftOperator(BinaryOperator):
    pass
