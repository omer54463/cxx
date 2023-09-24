from dataclasses import dataclass

from surgeon.expression.expression import Expression
from surgeon.expression.operator.operator import BinaryOperator, Operator, UnaryOperator


@dataclass
class SubscriptOperator(BinaryOperator):
    pass


@dataclass
class IndirectionOperator(UnaryOperator):
    pass


@dataclass
class AddressOfOperator(UnaryOperator):
    pass


@dataclass
class MemberOperator(Operator):
    operand: Expression
    identifier: str


@dataclass
class PointerMemberOperator(UnaryOperator):
    operand: Expression
    identifier: str
