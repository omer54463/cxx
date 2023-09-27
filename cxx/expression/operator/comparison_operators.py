from dataclasses import dataclass

from cxx.expression.operator.operator import BinaryOperator


@dataclass
class EqualsOperator(BinaryOperator):
    pass


@dataclass
class NotEqualsOperator(BinaryOperator):
    pass


@dataclass
class LesserOperator(BinaryOperator):
    pass


@dataclass
class GreaterOperator(BinaryOperator):
    pass


@dataclass
class LesserEqualsOperator(BinaryOperator):
    pass


@dataclass
class GreaterEqualsOperator(BinaryOperator):
    pass


@dataclass
class ThreeWayComparisonOperator(BinaryOperator):
    pass
