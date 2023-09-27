from dataclasses import dataclass

from cxx.expression.operator.access_operators import (
    DereferenceOperator,
    ReferenceOperator,
    SubscriptOperator,
)
from cxx.expression.operator.arithmetic_operators import (
    AdditionOperator,
    BinaryAndOperator,
    BinaryNotOperator,
    BinaryOrOperator,
    BinaryXorOperator,
    DivisionOperator,
    LeftShiftOperator,
    MinusOperator,
    MultiplicationOperator,
    PlusOperator,
    RemainderOperator,
    RightShiftOperator,
    SubtractionOperator,
)
from cxx.expression.operator.assignment_operators import (
    AdditionAssignmentOperator,
    AssignmentOperator,
    BinaryAndAssignmentOperator,
    BinaryNotAssignmentOperator,
    BinaryOrAssignmentOperator,
    BinaryXorAssignmentOperator,
    DivisionAssignmentOperator,
    LeftShiftAssignmentOperator,
    MultiplicationAssignmentOperator,
    RemainderAssignmentOperator,
    RightShiftAssignmentOperator,
    SubtractionAssignmentOperator,
)
from cxx.expression.operator.comparison_operators import (
    EqualsOperator,
    GreaterEqualsOperator,
    GreaterOperator,
    LesserEqualsOperator,
    LesserOperator,
    NotEqualsOperator,
    ThreeWayComparisonOperator,
)
from cxx.expression.operator.increment_decrement_operators import (
    PostDecrementOperator,
    PostIncrementOperator,
    PreDecrementOperator,
    PreIncrementOperator,
)
from cxx.expression.operator.logic_operators import (
    AndOperator,
    NotOperator,
    OrOperator,
)
from cxx.expression.operator.operator import (
    BinaryOperator,
    TrinaryOperator,
    UnaryOperator,
)
from cxx.expression.operator.other_operators import (
    CommaOperator,
    ConditionalOperator,
)


@dataclass
class UnaryOperatorSymbols:
    before: str | None = None
    after: str | None = None


UNARY_OPERATOR_SYMBOLS: dict[type[UnaryOperator], UnaryOperatorSymbols] = {
    DereferenceOperator: UnaryOperatorSymbols(before="*"),
    ReferenceOperator: UnaryOperatorSymbols(before="&"),
    PlusOperator: UnaryOperatorSymbols(before="+"),
    MinusOperator: UnaryOperatorSymbols(before="-"),
    BinaryNotOperator: UnaryOperatorSymbols(before="~"),
    PreIncrementOperator: UnaryOperatorSymbols(before="++"),
    PreDecrementOperator: UnaryOperatorSymbols(before="--"),
    PostIncrementOperator: UnaryOperatorSymbols(after="++"),
    PostDecrementOperator: UnaryOperatorSymbols(after="--"),
    NotOperator: UnaryOperatorSymbols(before="!"),
}


@dataclass
class BinaryOperatorSymbols:
    before: str | None = None
    between: str | None = None
    after: str | None = None


BINARY_OPERATOR_SYMBOLS: dict[type[BinaryOperator], BinaryOperatorSymbols] = {
    SubscriptOperator: BinaryOperatorSymbols(between="[", after="]"),
    AdditionOperator: BinaryOperatorSymbols(between="+"),
    SubtractionOperator: BinaryOperatorSymbols(between="-"),
    MultiplicationOperator: BinaryOperatorSymbols(between="*"),
    DivisionOperator: BinaryOperatorSymbols(between="/"),
    RemainderOperator: BinaryOperatorSymbols(between="%"),
    BinaryAndOperator: BinaryOperatorSymbols(between="&"),
    BinaryOrOperator: BinaryOperatorSymbols(between="|"),
    BinaryXorOperator: BinaryOperatorSymbols(between="^"),
    LeftShiftOperator: BinaryOperatorSymbols(between="<<"),
    RightShiftOperator: BinaryOperatorSymbols(between=">>"),
    AssignmentOperator: BinaryOperatorSymbols(between="="),
    AdditionAssignmentOperator: BinaryOperatorSymbols(between="+="),
    SubtractionAssignmentOperator: BinaryOperatorSymbols(between="-="),
    MultiplicationAssignmentOperator: BinaryOperatorSymbols(between="*="),
    DivisionAssignmentOperator: BinaryOperatorSymbols(between="/="),
    RemainderAssignmentOperator: BinaryOperatorSymbols(between="%="),
    BinaryNotAssignmentOperator: BinaryOperatorSymbols(between="~="),
    BinaryAndAssignmentOperator: BinaryOperatorSymbols(between="&="),
    BinaryOrAssignmentOperator: BinaryOperatorSymbols(between="|="),
    BinaryXorAssignmentOperator: BinaryOperatorSymbols(between="^="),
    LeftShiftAssignmentOperator: BinaryOperatorSymbols(between="<<="),
    RightShiftAssignmentOperator: BinaryOperatorSymbols(between=">>="),
    EqualsOperator: BinaryOperatorSymbols(between="=="),
    NotEqualsOperator: BinaryOperatorSymbols(between="!="),
    LesserOperator: BinaryOperatorSymbols(between="<"),
    GreaterOperator: BinaryOperatorSymbols(between=">"),
    LesserEqualsOperator: BinaryOperatorSymbols(between="<="),
    GreaterEqualsOperator: BinaryOperatorSymbols(between=">="),
    ThreeWayComparisonOperator: BinaryOperatorSymbols(between="<=>"),
    AndOperator: BinaryOperatorSymbols(between="&&"),
    OrOperator: BinaryOperatorSymbols(between="||"),
    CommaOperator: BinaryOperatorSymbols(between=","),
}


@dataclass
class TrinaryOperatorSymbols:
    before: str | None = None
    left: str | None = None
    right: str | None = None
    after: str | None = None


TRINARY_OPERATOR_SYMBOLS: dict[type[TrinaryOperator], TrinaryOperatorSymbols] = {
    ConditionalOperator: TrinaryOperatorSymbols(left="?", right=":"),
}
