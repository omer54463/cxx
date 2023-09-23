from collections.abc import Iterable
from itertools import chain

from surgeon.expression.expression import Expression
from surgeon.serialize.serialize_declaration import serialize_declaration
from surgeon.serialize.serialize_expression import (
    serialize_expression,
    serialize_optional_expression,
)
from surgeon.serialize.utility import flatten_lines
from surgeon.statement.compound_statement import CompountStatement
from surgeon.statement.declaration_statement import DeclarationStatement
from surgeon.statement.expression_statement import ExpressionStatement
from surgeon.statement.iteration_statement.do_while_statement import DoWhileStatement
from surgeon.statement.iteration_statement.for_range_statement import ForRangeStatement
from surgeon.statement.iteration_statement.for_statement import ForStatement
from surgeon.statement.iteration_statement.iteration_statement import IterationStatement
from surgeon.statement.iteration_statement.while_statement import WhileStatement
from surgeon.statement.jump_statement.break_statement import BreakStatement
from surgeon.statement.jump_statement.continue_statement import ContinueStatement
from surgeon.statement.jump_statement.goto_statement import GotoStatement
from surgeon.statement.jump_statement.jump_statement import JumpStatement
from surgeon.statement.jump_statement.return_statement import ReturnStatement
from surgeon.statement.labeled_statement.case_statement import CaseStatement
from surgeon.statement.labeled_statement.default_statement import DefaultStatement
from surgeon.statement.labeled_statement.label_statement import (
    LabelStatement,
)
from surgeon.statement.labeled_statement.labeled_statement import LabeledStatement
from surgeon.statement.null_statement import NullStatement
from surgeon.statement.selection_statement.if_statement import IfStatement
from surgeon.statement.selection_statement.selection_statement import SelectionStatement
from surgeon.statement.selection_statement.switch_statement import SwitchStatement
from surgeon.statement.statement import Statement


def serialize_statement(statement: Statement) -> Iterable[Iterable[str]]:
    match statement:
        case IterationStatement():
            yield from serialize_iteration_statement(statement)

        case JumpStatement():
            yield from serialize_jump_statement(statement)

        case LabeledStatement():
            yield from serialize_labeled_statement(statement)

        case SelectionStatement():
            yield from serialize_selection_statement(statement)

        case CompountStatement(content):
            yield ("{",)
            for sub_statement in statement.content:
                yield from serialize_statement(sub_statement)
            yield ("}",)

        case DeclarationStatement(content):
            yield from serialize_declaration(content)

        case ExpressionStatement(content):
            yield chain(serialize_expression(content), (";",))

        case NullStatement():
            yield (";",)

        case _:
            raise TypeError(f"Unexpected type {type(statement)}")


def serialize_optional_statement(
    statement: Statement | None,
) -> Iterable[Iterable[str]]:
    if statement is not None:
        yield from serialize_statement(statement)


def serialize_iteration_statement(
    statement: IterationStatement,
) -> Iterable[Iterable[str]]:
    match statement:
        case DoWhileStatement(content, condition):
            yield ("do",)
            yield from serialize_statement(content)
            yield chain(("while", "("), serialize_expression(condition), (")", ";"))

        case ForRangeStatement(initializer, value, range, content):
            yield chain(
                ("for", "("),
                flatten_lines(serialize_optional_statement(initializer)),
                flatten_lines(serialize_declaration(value)),
                (":",),
                serialize_expression(range),
                (")"),
            )
            yield from serialize_statement(content)

        case ForStatement(initializer, condition, progression, content):
            yield chain(
                ("for", "("),
                flatten_lines(serialize_statement(initializer)),
                serialize_optional_expression(condition),
                (";",),
                serialize_optional_expression(progression),
                (")"),
            )
            yield from serialize_statement(content)

        case WhileStatement(condition, content):
            yield chain(("while", "("), serialize_expression(condition), (")",))
            yield from serialize_statement(content)

        case _:
            raise TypeError(f"Unexpected type {type(statement)}")


def serialize_jump_statement(
    statement: JumpStatement,
) -> Iterable[Iterable[str]]:
    match statement:
        case BreakStatement():
            yield ("break", ";")

        case ContinueStatement():
            yield ("continue", ";")

        case GotoStatement(identifier):
            yield ("goto", identifier, ";")

        case ReturnStatement(None):
            yield ("return", ";")

        case ReturnStatement(Expression() as expression):
            yield chain(("return",), serialize_expression(expression), (";",))

        case _:
            raise TypeError(f"Unexpected type {type(statement)}")


def serialize_labeled_statement(
    statement: LabeledStatement,
) -> Iterable[Iterable[str]]:
    match statement:
        case CaseStatement(value):
            yield chain(("case",), serialize_expression(value), (":",))

        case DefaultStatement():
            yield ("default", ":")

        case LabelStatement(identifier):
            yield (identifier, ":")

        case _:
            raise TypeError(f"Unexpected type {type(statement)}")


def serialize_selection_statement(
    statement: SelectionStatement,
) -> Iterable[Iterable[str]]:
    match statement:
        case IfStatement(
            constexpr,
            initializer,
            condition,
            content,
            else_content,
        ):
            yield chain(
                ("if",),
                ("constexpr",) if constexpr else (),
                ("(",),
                flatten_lines(serialize_optional_statement(initializer)),
                serialize_expression(condition),
                (")",),
            )
            yield from serialize_statement(content)

            if else_content is not None:
                yield ("else",)
                yield from serialize_statement(else_content)

        case SwitchStatement(initializer, value, content):
            yield chain(
                ("switch", "("),
                flatten_lines(serialize_optional_statement(initializer)),
                serialize_expression(value),
                (")",),
            )
            yield from serialize_statement(content)

        case _:
            raise TypeError(f"Unexpected type {type(statement)}")
