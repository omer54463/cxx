from collections.abc import Iterable
from dataclasses import dataclass

import pytest
import pytest_mock

from surgeon.declaration.declaration import Declaration
from surgeon.expression.expression import Expression
from surgeon.serialize import (
    serialize_declaration as serialize_declaration_module,
)
from surgeon.serialize import (
    serialize_expression as serialize_expression_module,
)
from surgeon.serialize import (
    serialize_statement as serialize_statement_module,
)
from surgeon.serialize.serialize_statement import serialize_statement
from surgeon.statement.compound_statement import CompountStatement
from surgeon.statement.declaration_statement import DeclarationStatement
from surgeon.statement.expression_statement import ExpressionStatement
from surgeon.statement.iteration_statement.do_while_statement import DoWhileStatement
from surgeon.statement.iteration_statement.for_range_expression import ForRangeStatement
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


@dataclass
class FakeExpression(Expression):
    content: str


def fake_serialize_expression(expression: Expression) -> Iterable[str]:
    assert isinstance(expression, FakeExpression), "Invalid expression type in test"
    yield expression.content


@pytest.fixture(autouse=True, scope="module")
def mock_serialize_expression(module_mocker: pytest_mock.MockerFixture) -> None:
    for patch_module in (serialize_statement_module, serialize_expression_module):
        module_mocker.patch.object(
            patch_module,
            "serialize_expression",
            wraps=fake_serialize_expression,
        )


@dataclass
class FakeDeclaration(Declaration):
    content: str


def fake_serialize_declaration(declaration: Declaration) -> Iterable[str]:
    assert isinstance(declaration, FakeDeclaration), "Invalid declaration type in test"
    yield declaration.content


@pytest.fixture(autouse=True, scope="module")
def mock_serialize_declaration(module_mocker: pytest_mock.MockerFixture) -> None:
    for patch_module in (serialize_statement_module, serialize_declaration_module):
        module_mocker.patch.object(
            patch_module,
            "serialize_declaration",
            wraps=fake_serialize_declaration,
        )


BASIC_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        NullStatement(),
        [
            [";"],
        ],
    ),
    (
        ExpressionStatement(FakeExpression("test")),
        [
            ["test", ";"],
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
        DeclarationStatement(
            FakeDeclaration("declaration"),
        ),
        [
            ["declaration", ";"],
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
            FakeDeclaration("value"),
            FakeExpression("range"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["for", "(", "value", ":", "range", ")"],
            ["content", ";"],
        ],
    ),
    (
        ForStatement(
            ExpressionStatement(FakeExpression("initialize")),
            ExpressionStatement(FakeExpression("content")),
            FakeExpression("condition"),
        ),
        [
            ["for", "(", "initialize", ";", "condition", ";", ")"],
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
        ReturnStatement(),
        [
            ["return", ";"],
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
        GotoTargetStatement("label"),
        [
            ["label", ":"],
        ],
    ),
)

SELECTION_STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    (
        IfConstexprElseStatement(
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
            ExpressionStatement(FakeExpression("else_content")),
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
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["if", "constexpr", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
    (
        IfElseStatement(
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
            ExpressionStatement(FakeExpression("else_content")),
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
            FakeExpression("condition"),
            ExpressionStatement(FakeExpression("content")),
        ),
        [
            ["if", "(", "condition", ")"],
            ["content", ";"],
        ],
    ),
)

STATEMENT_TEST_DATA: Iterable[tuple[Statement, list[list[str]]]] = (
    *BASIC_STATEMENT_TEST_DATA,
    *ITERATION_STATEMENT_TEST_DATA,
    *JUMP_STATEMENT_TEST_DATA,
    *LABELED_STATEMENT_TEST_DATA,
    *SELECTION_STATEMENT_TEST_DATA,
)


@pytest.mark.parametrize(("statement", "expected"), STATEMENT_TEST_DATA)
def test_serialize_statement(statement: Statement, expected: list[list[str]]) -> None:
    statement_lines = serialize_statement(statement)
    statement_lines_as_lists = [list(line) for line in statement_lines]

    assert statement_lines_as_lists == expected
