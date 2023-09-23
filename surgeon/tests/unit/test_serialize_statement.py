from collections.abc import Iterable
from itertools import chain

import pytest

from surgeon.serialize.serialize_statement import serialize_statement
from surgeon.statement.compound_statement import CompountStatement
from surgeon.statement.declaration_statement import DeclarationStatement
from surgeon.statement.expression_statement import ExpressionStatement
from surgeon.statement.iteration_statement.do_while_statement import DoWhileStatement
from surgeon.statement.iteration_statement.for_range_statement import ForRangeStatement
from surgeon.statement.iteration_statement.for_statement import ForStatement
from surgeon.statement.iteration_statement.while_statement import WhileStatement
from surgeon.statement.jump_statement.break_statement import BreakStatement
from surgeon.statement.jump_statement.continue_statement import ContinueStatement
from surgeon.statement.jump_statement.goto_statement import GotoStatement
from surgeon.statement.jump_statement.return_statement import ReturnStatement
from surgeon.statement.labeled_statement.case_statement import CaseStatement
from surgeon.statement.labeled_statement.default_statement import DefaultStatement
from surgeon.statement.labeled_statement.label_statement import (
    LabelStatement,
)
from surgeon.statement.null_statement import NullStatement
from surgeon.statement.selection_statement.if_else_statement import IfElseStatement
from surgeon.statement.selection_statement.if_statement import IfStatement
from surgeon.statement.selection_statement.switch_statement import SwitchStatement
from surgeon.statement.statement import Statement
from surgeon.tests.unit.mocks.mock_serialize_declaration import FakeDeclaration
from surgeon.tests.unit.mocks.mock_serialize_expression import FakeExpression
from surgeon.tests.unit.mocks.mock_serialize_initializer import FakeInitializer

BASIC_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        NullStatement(),
        [
            [";"],
        ],
    ),
    (
        ExpressionStatement(FakeExpression("expression")),
        [
            ["expression", ";"],
        ],
    ),
    (
        CompountStatement(
            [
                ExpressionStatement(FakeExpression("statement_1")),
                ExpressionStatement(FakeExpression("statement_2")),
            ],
        ),
        [
            ["{"],
            ["statement_1", ";"],
            ["statement_2", ";"],
            ["}"],
        ],
    ),
    (
        DeclarationStatement(FakeDeclaration("declaration")),
        [
            ["declaration"],
        ],
    ),
)

ITERATION_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        DoWhileStatement(
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["do"],
            ["content", ";"],
            ["while", "(", "condition", ")", ";"],
        ],
    ),
    (
        ForRangeStatement(
            ExpressionStatement(FakeExpression("initializer")),
            FakeDeclaration("value"),
            FakeExpression("range"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", "value", ":", "range", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForRangeStatement(
            initializer=None,
            value=FakeDeclaration("value"),
            range=FakeExpression("range"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "value", ":", "range", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            ExpressionStatement(FakeExpression("initializer")),
            FakeExpression("condition"),
            FakeExpression("progression"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", "condition", ";", "progression", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            ExpressionStatement(FakeExpression("initializer")),
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
            ExpressionStatement(FakeExpression("initializer")),
            FakeExpression("condition"),
            progression=None,
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", "condition", ";", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            ExpressionStatement(FakeExpression("initializer")),
            condition=None,
            progression=None,
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "initializer", ";", ";", ")"],
            ["content", ";"],
        ],
    ),
    (
        WhileStatement(
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["while", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
)

JUMP_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
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
    (
        ReturnStatement(FakeInitializer("initializer")),
        [
            ["return", "initializer", ";"],
        ],
    ),
)

LABELED_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
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

SELECTION_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        IfStatement(
            constexpr=True,
            initializer=ExpressionStatement(FakeExpression("initializer")),
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["if", "constexpr", "(", "initializer", ";", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfElseStatement(
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
        ),
        [
            ["if", "(", "initializer", ";", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfElseStatement(
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
            initializer=None,
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["if", "constexpr", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfElseStatement(
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
        IfStatement(
            constexpr=False,
            initializer=None,
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["if", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfElseStatement(
            constexpr=False,
            initializer=None,
            condition=FakeExpression("condition"),
            content=ExpressionStatement(FakeExpression("content")),
            else_content=ExpressionStatement(FakeExpression("else_content")),
        ),
        [
            ["if", "(", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        SwitchStatement(
            ExpressionStatement(FakeExpression("initializer")),
            FakeExpression("value"),
            ExpressionStatement(FakeExpression("content")),
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


@pytest.mark.usefixtures(
    "mock_serialize_expression",
    "mock_serialize_declaration",
    "mock_serialize_initializer",
)
@pytest.mark.parametrize(("statement", "expected"), STATEMENT_TEST_DATA)
def test_serialize_statement(statement: Statement, expected: list[list[str]]) -> None:
    statement_lines = serialize_statement(statement)
    statement_lines_as_lists = [list(line) for line in statement_lines]

    assert statement_lines_as_lists == expected
