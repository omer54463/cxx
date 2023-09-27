from collections.abc import Iterable
from itertools import chain

import pytest

from cxx.serialize.serialize_statement import serialize_statement
from cxx.statement.compound_statement import CompountStatement
from cxx.statement.declaration_statement import DeclarationStatement
from cxx.statement.expression_statement import ExpressionStatement
from cxx.statement.iteration_statement.do_while_statement import DoWhileStatement
from cxx.statement.iteration_statement.for_statement import ForStatement
from cxx.statement.iteration_statement.iteration_statement import IterationStatement
from cxx.statement.iteration_statement.while_statement import WhileStatement
from cxx.statement.jump_statement.break_statement import BreakStatement
from cxx.statement.jump_statement.continue_statement import ContinueStatement
from cxx.statement.jump_statement.goto_statement import GotoStatement
from cxx.statement.jump_statement.jump_statement import JumpStatement
from cxx.statement.jump_statement.return_statement import ReturnStatement
from cxx.statement.labeled_statement.case_statement import CaseStatement
from cxx.statement.labeled_statement.default_statement import DefaultStatement
from cxx.statement.labeled_statement.label_statement import (
    LabelStatement,
)
from cxx.statement.labeled_statement.labeled_statement import LabeledStatement
from cxx.statement.null_statement import NullStatement
from cxx.statement.selection_statement.if_statement import IfStatement
from cxx.statement.selection_statement.selection_statement import SelectionStatement
from cxx.statement.selection_statement.switch_statement import SwitchStatement
from cxx.statement.statement import Statement
from cxx.tests.unit.flatten_lines import flatten_lines
from cxx.tests.unit.mocks.mock_serialize_declaration import FakeDeclaration
from cxx.tests.unit.mocks.mock_serialize_expression import FakeExpression

BASIC_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        NullStatement(),
        [
            [";"],
        ],
    ),
    (
        ExpressionStatement(FakeExpression("content")),
        [
            ["content", ";"],
        ],
    ),
    (
        CompountStatement([]),
        [
            ["{"],
            ["}"],
        ],
    ),
    (
        CompountStatement([ExpressionStatement(FakeExpression("content"))]),
        [
            ["{"],
            ["content", ";"],
            ["}"],
        ],
    ),
    (
        DeclarationStatement(FakeDeclaration("declaration")),
        [
            ["declaration", ";"],
        ],
    ),
)

ITERATION_STATEMENT_TEST_DATA: Iterable[tuple[IterationStatement, list[list[str]]]] = (
    (
        DoWhileStatement(
            content=ExpressionStatement(FakeExpression("content")),
            condition=FakeExpression("condition"),
        ),
        [
            ["do"],
            ["content", ";"],
            ["while", "(", "condition", ")", ";"],
        ],
    ),
    (
        ForStatement(
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            progression=FakeExpression("progression"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", "condition", ";", "progression", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=None,
            progression=FakeExpression("progression"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", ";", "progression", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            progression=None,
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", "condition", ";", ")"],
            ["content", ";"],
        ],
    ),
    (
        WhileStatement(
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["while", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
)

JUMP_STATEMENT_TEST_DATA: Iterable[tuple[JumpStatement, list[list[str]]]] = (
    (
        BreakStatement(),
        [
            ["break", ";"],
        ],
    ),
    (
        ContinueStatement(),
        [
            ["continue", ";"],
        ],
    ),
    (
        GotoStatement("identifier"),
        [
            ["goto", "identifier", ";"],
        ],
    ),
    (
        ReturnStatement(None),
        [
            ["return", ";"],
        ],
    ),
    (
        ReturnStatement(FakeExpression("expression")),
        [
            ["return", "expression", ";"],
        ],
    ),
)

LABELED_STATEMENT_TEST_DATA: Iterable[tuple[LabeledStatement, list[list[str]]]] = (
    (
        CaseStatement(FakeExpression("value")),
        [
            ["case", "value", ":"],
        ],
    ),
    (
        DefaultStatement(),
        [
            ["default", ":"],
        ],
    ),
    (
        LabelStatement("label"),
        [
            ["label", ":"],
        ],
    ),
)

SELECTION_STATEMENT_TEST_DATA: Iterable[tuple[SelectionStatement, list[list[str]]]] = (
    (
        IfStatement(
            constexpr=True,
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
            else_content=ExpressionStatement(FakeExpression("else_content")),
        ),
        [
            ["if", "constexpr", "(", "initializer", ";", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        IfStatement(
            constexpr=False,
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
            else_content=ExpressionStatement(FakeExpression("else_content")),
        ),
        [
            ["if", "(", "initializer", ";", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        IfStatement(
            constexpr=True,
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
            else_content=None,
        ),
        [
            ["if", "constexpr", "(", "initializer", ";", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfStatement(
            constexpr=True,
            initializer=None,
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
            else_content=ExpressionStatement(FakeExpression("else_content")),
        ),
        [
            ["if", "constexpr", "(", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        SwitchStatement(
            initializer=ExpressionStatement(FakeExpression("initializer")),
            value=FakeExpression("value"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["switch", "(", "initializer", ";", "value", ")"],
            ["content", ";"],
        ],
    ),
    (
        SwitchStatement(
            initializer=None,
            value=FakeExpression("value"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["switch", "(", "value", ")"],
            ["content", ";"],
        ],
    ),
)

STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = chain(
    BASIC_STATEMENT_TEST_DATA,
    ITERATION_STATEMENT_TEST_DATA,
    JUMP_STATEMENT_TEST_DATA,
    LABELED_STATEMENT_TEST_DATA,
    SELECTION_STATEMENT_TEST_DATA,
)


@pytest.mark.usefixtures("mock_serialize_expression", "mock_serialize_declaration")
@pytest.mark.parametrize(("statement", "expected_lines"), STATEMENT_TEST_DATA)
def test_serialize_statement(
    statement: Statement,
    expected_lines: list[list[str]],
) -> None:
    result = list(serialize_statement(statement))
    expected = list(flatten_lines(expected_lines))

    assert result == expected
