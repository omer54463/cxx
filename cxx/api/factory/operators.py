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
from cxx.expression.operator.other_operators import (
    CastMode,
    CastOperator,
    CCastOperator,
    CommaOperator,
    ConditionalOperator,
    FunctionCallOperator,
)


class AccessOperators:
    def subscript(self, left: Expression, right: Expression) -> SubscriptOperator:
        return SubscriptOperator(left, right)

    def dereference(self, operand: Expression) -> DereferenceOperator:
        return DereferenceOperator(operand)

    def reference(self, operand: Expression) -> ReferenceOperator:
        return ReferenceOperator(operand)

    def member(
        self,
        operand: Expression,
        identifier: str,
        dereference: bool = False,
    ) -> MemberOperator:
        return MemberOperator(operand, identifier, dereference)


class ArithmeticOperators:
    def plus(self, operand: Expression) -> PlusOperator:
        return PlusOperator(operand)

    def minus(self, operand: Expression) -> MinusOperator:
        return MinusOperator(operand)

    def add(self, left: Expression, right: Expression) -> AdditionOperator:
        return AdditionOperator(left, right)

    def subtract(self, left: Expression, right: Expression) -> SubtractionOperator:
        return SubtractionOperator(left, right)

    def multiply(self, left: Expression, right: Expression) -> MultiplicationOperator:
        return MultiplicationOperator(left, right)

    def divide(self, left: Expression, right: Expression) -> DivisionOperator:
        return DivisionOperator(left, right)

    def remainder(self, left: Expression, right: Expression) -> RemainderOperator:
        return RemainderOperator(left, right)

    def binary_not(self, operand: Expression) -> BinaryNotOperator:
        return BinaryNotOperator(operand)

    def binary_and(self, left: Expression, right: Expression) -> BinaryAndOperator:
        return BinaryAndOperator(left, right)

    def binary_or(self, left: Expression, right: Expression) -> BinaryOrOperator:
        return BinaryOrOperator(left, right)

    def binary_xor(self, left: Expression, right: Expression) -> BinaryXorOperator:
        return BinaryXorOperator(left, right)

    def left_shift(self, left: Expression, right: Expression) -> LeftShiftOperator:
        return LeftShiftOperator(left, right)

    def right_shift(self, left: Expression, right: Expression) -> RightShiftOperator:
        return RightShiftOperator(left, right)


class AssignmentOperators:
    def direct(self, left: Expression, right: Expression) -> AssignmentOperator:
        return AssignmentOperator(left, right)

    def add(self, left: Expression, right: Expression) -> AdditionAssignmentOperator:
        return AdditionAssignmentOperator(left, right)

    def subtract(
        self,
        left: Expression,
        right: Expression,
    ) -> SubtractionAssignmentOperator:
        return SubtractionAssignmentOperator(left, right)

    def multiply(
        self,
        left: Expression,
        right: Expression,
    ) -> MultiplicationAssignmentOperator:
        return MultiplicationAssignmentOperator(left, right)

    def divide(self, left: Expression, right: Expression) -> DivisionAssignmentOperator:
        return DivisionAssignmentOperator(left, right)

    def remainder(
        self,
        left: Expression,
        right: Expression,
    ) -> RemainderAssignmentOperator:
        return RemainderAssignmentOperator(left, right)

    def binary_not(
        self,
        left: Expression,
        right: Expression,
    ) -> BinaryNotAssignmentOperator:
        return BinaryNotAssignmentOperator(left, right)

    def binary_and(
        self,
        left: Expression,
        right: Expression,
    ) -> BinaryAndAssignmentOperator:
        return BinaryAndAssignmentOperator(left, right)

    def binary_or(
        self,
        left: Expression,
        right: Expression,
    ) -> BinaryOrAssignmentOperator:
        return BinaryOrAssignmentOperator(left, right)

    def binary_xor(
        self,
        left: Expression,
        right: Expression,
    ) -> BinaryXorAssignmentOperator:
        return BinaryXorAssignmentOperator(left, right)

    def left_shift(
        self,
        left: Expression,
        right: Expression,
    ) -> LeftShiftAssignmentOperator:
        return LeftShiftAssignmentOperator(left, right)

    def right_shift(
        self,
        left: Expression,
        right: Expression,
    ) -> RightShiftAssignmentOperator:
        return RightShiftAssignmentOperator(left, right)


class ComparisonOperators:
    def equals(self, left: Expression, right: Expression) -> EqualsOperator:
        return EqualsOperator(left, right)

    def not_equals(self, left: Expression, right: Expression) -> NotEqualsOperator:
        return NotEqualsOperator(left, right)

    def lesser(self, left: Expression, right: Expression) -> LesserOperator:
        return LesserOperator(left, right)

    def greater(self, left: Expression, right: Expression) -> GreaterOperator:
        return GreaterOperator(left, right)

    def lesser_equals(
        self,
        left: Expression,
        right: Expression,
    ) -> LesserEqualsOperator:
        return LesserEqualsOperator(left, right)

    def greater_equals(
        self,
        left: Expression,
        right: Expression,
    ) -> GreaterEqualsOperator:
        return GreaterEqualsOperator(left, right)

    def three_way(
        self,
        left: Expression,
        right: Expression,
    ) -> ThreeWayComparisonOperator:
        return ThreeWayComparisonOperator(left, right)


class IncrementDecrementOperators:
    def pre_increment(self, operand: Expression) -> PreIncrementOperator:
        return PreIncrementOperator(operand)

    def pre_decrement(self, operand: Expression) -> PreDecrementOperator:
        return PreDecrementOperator(operand)

    def post_increment(self, operand: Expression) -> PostIncrementOperator:
        return PostIncrementOperator(operand)

    def post_decrement(self, operand: Expression) -> PostDecrementOperator:
        return PostDecrementOperator(operand)


class LogicOperators:
    def not_(self, operand: Expression) -> NotOperator:
        return NotOperator(operand)

    def and_(self, left: Expression, right: Expression) -> AndOperator:
        return AndOperator(left, right)

    def or_(self, left: Expression, right: Expression) -> OrOperator:
        return OrOperator(left, right)


class OtherOperatorFactory:
    def function_call(
        self,
        operand: Expression,
        arguments: list[Expression] | None = None,
    ) -> FunctionCallOperator:
        return FunctionCallOperator(operand, [] if arguments is None else arguments)

    def comma(self, left: Expression, right: Expression) -> CommaOperator:
        return CommaOperator(left, right)

    def conditional(
        self,
        left: Expression,
        middle: Expression,
        right: Expression,
    ) -> ConditionalOperator:
        return ConditionalOperator(left, middle, right)

    def c_cast(self, type: str, operand: Expression) -> CCastOperator:
        return CCastOperator(type, operand)

    def cast(self, mode: CastMode, type: str, operand: Expression) -> CastOperator:
        return CastOperator(mode, type, operand)


class Operators:
    access: AccessOperators
    arithmetic: ArithmeticOperators
    assignment: AssignmentOperators
    comparison: ComparisonOperators
    inc_dec: IncrementDecrementOperators
    logic: LogicOperators
    other: OtherOperatorFactory

    def __init__(self) -> None:
        self.access = AccessOperators()
        self.arithmetic = ArithmeticOperators()
        self.assignment = AssignmentOperators()
        self.comparison = ComparisonOperators()
        self.inc_dec = IncrementDecrementOperators()
        self.logic = LogicOperators()
        self.other = OtherOperatorFactory()
