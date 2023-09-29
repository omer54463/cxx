from collections.abc import Iterable
from itertools import chain

import pytest

from cxx.expression.expression import Expression
from cxx.expression.literal.boolean_literal import BooleanLiteral
from cxx.expression.literal.character_literal import CharacterLiteral
from cxx.expression.literal.identifier_literal import IdentifierLiteral
from cxx.expression.literal.integer_literal import IntegerBase, IntegerLiteral
from cxx.expression.literal.string_literal import StringLiteral
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
from cxx.serialize.serialize_expression import serialize_expression

LITERAL_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (BooleanLiteral(True), ["true"]),
    (BooleanLiteral(False), ["false"]),
    (IdentifierLiteral("identifier"), ["identifier"]),
    (IntegerLiteral(0b1010101, IntegerBase.BINARY), ["0b1010101"]),
    (IntegerLiteral(0o707070, IntegerBase.OCTAL), ["0o707070"]),
    (IntegerLiteral(909090, IntegerBase.DECIMAL), ["909090"]),
    (IntegerLiteral(0xF0F0F0, IntegerBase.HEXADECIMAL), ["0xF0F0F0"]),
    (StringLiteral("string", False), ['"string"']),
    (StringLiteral("string\nstring", False), ['"""string\nstring"""']),
    (StringLiteral("string", True), ['L"string"']),
    (StringLiteral("string\nstring", True), ['L"""string\nstring"""']),
    (CharacterLiteral("c"), ["'c'"]),
)

ACCESS_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        SubscriptOperator(
            left_operand=IdentifierLiteral("identifier"),
            right_operand=IdentifierLiteral("subscript"),
        ),
        ["identifier", "[", "subscript", "]"],
    ),
    (
        DereferenceOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["*", "identifier"],
    ),
    (
        ReferenceOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["&", "identifier"],
    ),
    (
        MemberOperator(
            operand=IdentifierLiteral("identifier"),
            identifier="member",
            dereference=False,
        ),
        ["identifier", ".", "member"],
    ),
    (
        MemberOperator(
            operand=IdentifierLiteral("identifier"),
            identifier="member",
            dereference=True,
        ),
        ["identifier", "->", "member"],
    ),
)

ARITHMETIC_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        PlusOperator(operand=IdentifierLiteral("identifier")),
        ["+", "identifier"],
    ),
    (
        MinusOperator(operand=IdentifierLiteral("identifier")),
        ["-", "identifier"],
    ),
    (
        AdditionOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "+", "right"],
    ),
    (
        SubtractionOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "-", "right"],
    ),
    (
        MultiplicationOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "*", "right"],
    ),
    (
        DivisionOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "/", "right"],
    ),
    (
        RemainderOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "%", "right"],
    ),
    (
        BinaryNotOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["~", "identifier"],
    ),
    (
        BinaryAndOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "&", "right"],
    ),
    (
        BinaryOrOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "|", "right"],
    ),
    (
        BinaryXorOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "^", "right"],
    ),
    (
        LeftShiftOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "<<", "right"],
    ),
    (
        RightShiftOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", ">>", "right"],
    ),
)

ASSIGNMENT_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        AssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "=", "right"],
    ),
    (
        AdditionAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "+=", "right"],
    ),
    (
        SubtractionAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "-=", "right"],
    ),
    (
        MultiplicationAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "*=", "right"],
    ),
    (
        DivisionAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "/=", "right"],
    ),
    (
        RemainderAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "%=", "right"],
    ),
    (
        BinaryNotAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "~=", "right"],
    ),
    (
        BinaryAndAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "&=", "right"],
    ),
    (
        BinaryOrAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "|=", "right"],
    ),
    (
        BinaryXorAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "^=", "right"],
    ),
    (
        LeftShiftAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "<<=", "right"],
    ),
    (
        RightShiftAssignmentOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", ">>=", "right"],
    ),
)

COMPARISON_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        EqualsOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "==", "right"],
    ),
    (
        NotEqualsOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "!=", "right"],
    ),
    (
        LesserOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "<", "right"],
    ),
    (
        GreaterOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", ">", "right"],
    ),
    (
        LesserEqualsOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "<=", "right"],
    ),
    (
        GreaterEqualsOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", ">=", "right"],
    ),
    (
        ThreeWayComparisonOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "<=>", "right"],
    ),
)

INCREMENT_DECREMENT_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        PreIncrementOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["++", "identifier"],
    ),
    (
        PreDecrementOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["--", "identifier"],
    ),
    (
        PostIncrementOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["identifier", "++"],
    ),
    (
        PostDecrementOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["identifier", "--"],
    ),
)

LOGIC_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        NotOperator(
            operand=IdentifierLiteral("identifier"),
        ),
        ["!", "identifier"],
    ),
    (
        AndOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "&&", "right"],
    ),
    (
        OrOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "||", "right"],
    ),
)

OTHER_OPERATOR_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        FunctionCallOperator(
            operand=IdentifierLiteral("identifier"),
            argument_operands=[],
        ),
        ["identifier", "(", ")"],
    ),
    (
        FunctionCallOperator(
            operand=IdentifierLiteral("identifier"),
            argument_operands=[
                IdentifierLiteral("identifier"),
            ],
        ),
        ["identifier", "(", "identifier", ")"],
    ),
    (
        FunctionCallOperator(
            operand=IdentifierLiteral("identifier"),
            argument_operands=[
                IdentifierLiteral("identifier"),
                IdentifierLiteral("identifier"),
            ],
        ),
        ["identifier", "(", "identifier", ",", "identifier", ")"],
    ),
    (
        CommaOperator(
            left_operand=IdentifierLiteral("left"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", ",", "right"],
    ),
    (
        ConditionalOperator(
            left_operand=IdentifierLiteral("left"),
            middle_operand=IdentifierLiteral("middle"),
            right_operand=IdentifierLiteral("right"),
        ),
        ["left", "?", "middle", ":", "right"],
    ),
    (
        CCastOperator(
            type="type",
            operand=IdentifierLiteral("identifier"),
        ),
        ["(", "type", ")", "identifier"],
    ),
    (
        CastOperator(
            type="type",
            operand=IdentifierLiteral("identifier"),
            mode=CastMode.STATIC,
        ),
        ["static_cast", "<", "type", ">", "(", "identifier", ")"],
    ),
    (
        CastOperator(
            type="type",
            operand=IdentifierLiteral("identifier"),
            mode=CastMode.DYNAMIC,
        ),
        ["dynamic_cast", "<", "type", ">", "(", "identifier", ")"],
    ),
    (
        CastOperator(
            type="type",
            operand=IdentifierLiteral("identifier"),
            mode=CastMode.CONST,
        ),
        ["const_cast", "<", "type", ">", "(", "identifier", ")"],
    ),
    (
        CastOperator(
            type="type",
            operand=IdentifierLiteral("identifier"),
            mode=CastMode.REINTERPRET,
        ),
        ["reinterpret_cast", "<", "type", ">", "(", "identifier", ")"],
    ),
)

PRECEDENCE_TEST_DATA: Iterable[tuple[Expression, list[str]]] = (
    (
        AdditionOperator(
            MultiplicationOperator(IdentifierLiteral("a"), IdentifierLiteral("b")),
            IdentifierLiteral("c"),
        ),
        ["a", "*", "b", "+", "c"],
    ),
    (
        MultiplicationOperator(
            IdentifierLiteral("a"),
            AdditionOperator(IdentifierLiteral("b"), IdentifierLiteral("c")),
        ),
        ["a", "*", "(", "b", "+", "c", ")"],
    ),
    (
        MultiplicationOperator(
            AdditionOperator(IdentifierLiteral("a"), IdentifierLiteral("b")),
            IdentifierLiteral("c"),
        ),
        ["(", "a", "+", "b", ")", "*", "c"],
    ),
    (
        CCastOperator("C", MemberOperator(IdentifierLiteral("a"), "b", False)),
        ["(", "C", ")", "a", ".", "b"],
    ),
    (
        MemberOperator(CCastOperator("C", IdentifierLiteral("a")), "b", False),
        ["(", "(", "C", ")", "a", ")", ".", "b"],
    ),
)

EXPRESSION_TEST_DATA: Iterable[tuple[Expression, list[str]]] = chain(
    LITERAL_TEST_DATA,
    ACCESS_OPERATOR_TEST_DATA,
    ARITHMETIC_OPERATOR_TEST_DATA,
    ASSIGNMENT_OPERATOR_TEST_DATA,
    COMPARISON_OPERATOR_TEST_DATA,
    INCREMENT_DECREMENT_OPERATOR_TEST_DATA,
    LOGIC_OPERATOR_TEST_DATA,
    OTHER_OPERATOR_TEST_DATA,
    PRECEDENCE_TEST_DATA,
)


@pytest.mark.parametrize(("expression", "expected"), EXPRESSION_TEST_DATA)
def test_serialize_expression(expression: Expression, expected: list[str]) -> None:
    result = list(serialize_expression(expression))

    assert result == expected
