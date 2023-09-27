from collections.abc import Iterable

from cxx.expression.expression import Expression
from cxx.expression.operator.access_operators import (
    DereferenceOperator,
    MemberOperator,
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
from cxx.expression.operator.operator import Operator
from cxx.expression.operator.other_operators import (
    CastOperator,
    CCastOperator,
    CommaOperator,
    ConditionalOperator,
    FunctionCallOperator,
)

PRECEDENCE_GROUPS: Iterable[Iterable[type[Operator]]] = (
    (
        PostIncrementOperator,
        PostDecrementOperator,
        FunctionCallOperator,
        CastOperator,
        SubscriptOperator,
        MemberOperator,
    ),
    (
        PreIncrementOperator,
        PreDecrementOperator,
        PlusOperator,
        MinusOperator,
        NotOperator,
        BinaryNotOperator,
        CCastOperator,
        DereferenceOperator,
        ReferenceOperator,
    ),
    (MultiplicationOperator, DivisionOperator, RemainderOperator),
    (AdditionOperator, SubtractionOperator),
    (LeftShiftOperator, RightShiftOperator),
    (ThreeWayComparisonOperator,),
    (LesserOperator, LesserEqualsOperator, GreaterOperator, GreaterEqualsOperator),
    (EqualsOperator, NotEqualsOperator),
    (BinaryAndOperator,),
    (BinaryXorOperator,),
    (BinaryOrOperator,),
    (AndOperator,),
    (OrOperator,),
    (
        ConditionalOperator,
        AssignmentOperator,
        AdditionAssignmentOperator,
        SubtractionAssignmentOperator,
        MultiplicationAssignmentOperator,
        DivisionAssignmentOperator,
        RemainderAssignmentOperator,
        LeftShiftAssignmentOperator,
        RightShiftAssignmentOperator,
        BinaryAndAssignmentOperator,
        BinaryXorAssignmentOperator,
        BinaryOrAssignmentOperator,
        BinaryNotAssignmentOperator,
    ),
    (CommaOperator,),
)


def get_precedence(expression_or_expression_type: Expression | type[Expression]) -> int:
    expression_type = (
        type(expression_or_expression_type)
        if isinstance(expression_or_expression_type, Expression)
        else expression_or_expression_type
    )

    if not issubclass(expression_type, Operator):
        return -1

    operator_type = expression_type

    for index, operator_type_group in enumerate(PRECEDENCE_GROUPS):
        if operator_type in operator_type_group:
            return index

    raise ValueError(f"Unknown operator precedence for {type(operator_type)}")
