from dataclasses import dataclass

from cxx.expression.operator.operator import BinaryOperator


@dataclass
class AssignmentOperator(BinaryOperator):
    pass


@dataclass
class AdditionAssignmentOperator(BinaryOperator):
    pass


@dataclass
class SubtractionAssignmentOperator(BinaryOperator):
    pass


@dataclass
class MultiplicationAssignmentOperator(BinaryOperator):
    pass


@dataclass
class DivisionAssignmentOperator(BinaryOperator):
    pass


@dataclass
class RemainderAssignmentOperator(BinaryOperator):
    pass


@dataclass
class BinaryNotAssignmentOperator(BinaryOperator):
    pass


@dataclass
class BinaryAndAssignmentOperator(BinaryOperator):
    pass


@dataclass
class BinaryOrAssignmentOperator(BinaryOperator):
    pass


@dataclass
class BinaryXorAssignmentOperator(BinaryOperator):
    pass


@dataclass
class LeftShiftAssignmentOperator(BinaryOperator):
    pass


@dataclass
class RightShiftAssignmentOperator(BinaryOperator):
    pass
