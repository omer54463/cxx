from collections.abc import Iterable

import pytest

from surgeon.expression.constant_expression import ConstantExpression
from surgeon.serialize.serialize_statement import serialize_statement
from surgeon.statement.compound_statement import CompountStatement
from surgeon.statement.expression_statement import ExpressionStatement
from surgeon.statement.iteration_statement.do_while_statement import DoWhileStatement
from surgeon.statement.iteration_statement.for_statement import ForStatement
from surgeon.statement.iteration_statement.while_statement import WhileStatement
from surgeon.statement.jump_statement.break_statement import BreakStatement
from surgeon.statement.jump_statement.continue_statement import ContinueStatement
from surgeon.statement.jump_statement.goto_statement import GotoStatement
from surgeon.statement.jump_statement.return_statement import ReturnStatement
from surgeon.statement.labeled_statement.case_statement import CaseStatement
from surgeon.statement.labeled_statement.default_statement import DefaultStatement
from surgeon.statement.labeled_statement.goto_target_statement import (
    GotoTargetStatement,
)
from surgeon.statement.null_statement import NullStatement
from surgeon.statement.selection_statement.if_constexpr_else_statement import (
    IfConstexprElseStatement,
)
from surgeon.statement.selection_statement.if_constexpr_statement import (
    IfConstexprStatement,
)
from surgeon.statement.selection_statement.if_else_statement import IfElseStatement
from surgeon.statement.selection_statement.if_statement import IfStatement
from surgeon.statement.statement import Statement

BASIC_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (NullStatement(), [[";"]]),
    (ExpressionStatement(ConstantExpression("test")), [["test", ";"]]),
    (
        CompountStatement(
            [
                ExpressionStatement(ConstantExpression("statement_1")),
                ExpressionStatement(ConstantExpression("statement_2")),
            ],
        ),
        [["{"], ["statement_1", ";"], ["statement_2", ";"], ["}"]],
    ),
)

ITERATION_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        DoWhileStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
        ),
        [["do"], ["content", ";"], ["while", "(", "condition", ")", ";"]],
    ),
    (
        ForStatement(
            ExpressionStatement(ConstantExpression("initialize")),
            ExpressionStatement(ConstantExpression("content")),
            ConstantExpression("condition"),
        ),
        [["for", "(", "initialize", ";", "condition", ";", ")"], ["content", ";"]],
    ),
    (
        WhileStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
        ),
        [["while", "(", "condition", ")"], ["content", ";"]],
    ),
)

JUMP_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (BreakStatement(), [["break", ";"]]),
    (ContinueStatement(), [["continue", ";"]]),
    (GotoStatement("identifier"), [["goto", "identifier", ";"]]),
    (ReturnStatement(), [["return", ";"]]),
)

LABELED_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (CaseStatement(ConstantExpression("value")), [["case", "value", ":"]]),
    (DefaultStatement(), [["default", ":"]]),
    (GotoTargetStatement("label"), [["label", ":"]]),
)

SELECTION_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        IfConstexprElseStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
            ExpressionStatement(ConstantExpression("else_content")),
        ),
        [
            ["if", "constexpr", "(", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        IfConstexprStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
        ),
        [["if", "constexpr", "(", "condition", ")"], ["content", ";"]],
    ),
    (
        IfElseStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
            ExpressionStatement(ConstantExpression("else_content")),
        ),
        [
            ["if", "(", "condition", ")"],
            ["content", ";"],
            ["else"],
            ["else_content", ";"],
        ],
    ),
    (
        IfStatement(
            ConstantExpression("condition"),
            ExpressionStatement(ConstantExpression("content")),
        ),
        [["if", "(", "condition", ")"], ["content", ";"]],
    ),
)

STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    *BASIC_STATEMENT_TEST_DATA,
    *ITERATION_STATEMENT_TEST_DATA,
    *JUMP_STATEMENT_TEST_DATA,
    *LABELED_STATEMENT_TEST_DATA,
    *SELECTION_STATEMENT_TEST_DATA,
)


def process_lines(lines: Iterable[Iterable[str]]) -> list[list[str]]:
    return [list(line) for line in lines]


@pytest.mark.parametrize(("statement", "expected"), STATEMENT_TEST_DATA)
def test_serialize_statement(statement: Statement, expected: list[list[str]]) -> None:
    assert process_lines(serialize_statement(statement)) == expected
