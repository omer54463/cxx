from dataclasses import dataclass

from surgeon.expression.operator.operator import UnaryOperator


@dataclass
class PreIncrementOperator(UnaryOperator):
    pass


@dataclass
class PreDecrementOperator(UnaryOperator):
    pass


@dataclass
class PostIncrementOperator(UnaryOperator):
    pass


@dataclass
class PostDecrementOperator(UnaryOperator):
    pass
