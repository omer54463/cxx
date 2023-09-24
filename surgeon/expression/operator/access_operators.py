from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.expression.operator.operator import BinaryOperator, Operator, UnaryOperator


@dataclass
class SubscriptOperator(BinaryOperator):
    pass


@dataclass
class DereferenceOperator(UnaryOperator):
    pass


@dataclass
class ReferenceOperator(UnaryOperator):
    pass


@dataclass
class MemberOperator(Operator):
    operand: Expression
    identifier: str
    dereference: bool
