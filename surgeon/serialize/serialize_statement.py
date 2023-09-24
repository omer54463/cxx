from collections.abc import Iterator

from surgeon.expression.expression import Expression
from surgeon.statement.compound_statement import CompountStatement
from surgeon.statement.declaration_statement import DeclarationStatement
from surgeon.statement.expression_statement import ExpressionStatement
from surgeon.statement.iteration_statement.do_while_statement import DoWhileStatement
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


def serialize_statement(statement: Statement) -> Iterator[str]:
    from surgeon.serialize.serialize_declaration import serialize_declaration
    from surgeon.serialize.serialize_expression import serialize_expression

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
            yield "{"
            for sub_statement in statement.content:
                yield from serialize_statement(sub_statement)
            yield "}"

        case DeclarationStatement(content):
            yield from serialize_declaration(content)

        case ExpressionStatement(content):
            yield from serialize_expression(content)
            yield ";"

        case NullStatement():
            yield ";"


def serialize_optional_statement(statement: Statement | None) -> Iterator[str]:
    if statement is not None:
        yield from serialize_statement(statement)


def serialize_iteration_statement(statement: IterationStatement) -> Iterator[str]:
    from surgeon.serialize.serialize_expression import (
        serialize_expression,
        serialize_optional_expression,
    )

    match statement:
        case DoWhileStatement(content, condition):
            yield "do"
            yield from serialize_statement(content)
            yield "while"
            yield "("
            yield from serialize_expression(condition)
            yield ")"
            yield ";"

        case ForStatement(initializer, condition, progression, content):
            yield "for"
            yield "("
            yield from serialize_statement(initializer)
            yield from serialize_optional_expression(condition)
            yield ";"
            yield from serialize_optional_expression(progression)
            yield ")"
            yield from serialize_statement(content)

        case WhileStatement(condition, content):
            yield "while"
            yield "("
            yield from serialize_expression(condition)
            yield ")"
            yield from serialize_statement(content)


def serialize_jump_statement(statement: JumpStatement) -> Iterator[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    match statement:
        case BreakStatement():
            yield "break"

        case ContinueStatement():
            yield "continue"

        case GotoStatement(identifier):
            yield "goto"
            yield identifier

        case ReturnStatement(None):
            yield "return"

        case ReturnStatement(Expression() as expression):
            yield "return"
            yield from serialize_expression(expression)

    yield ";"


def serialize_labeled_statement(statement: LabeledStatement) -> Iterator[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    match statement:
        case CaseStatement(value):
            yield "case"
            yield from serialize_expression(value)

        case DefaultStatement():
            yield "default"

        case LabelStatement(identifier):
            yield identifier

    yield ":"


def serialize_selection_statement(statement: SelectionStatement) -> Iterator[str]:
    from surgeon.serialize.serialize_expression import serialize_expression

    match statement:
        case IfStatement(
            constexpr,
            initializer,
            condition,
            content,
            else_content,
        ):
            yield "if"
            if constexpr:
                yield "constexpr"
            yield "("
            yield from serialize_optional_statement(initializer)
            yield from serialize_expression(condition)
            yield ")"
            yield from serialize_statement(content)

            if else_content is not None:
                yield "else"
                yield from serialize_statement(else_content)

        case SwitchStatement(initializer, value, content):
            yield "switch"
            yield "("
            yield from serialize_optional_statement(initializer)
            yield from serialize_expression(value)
            yield ")"
            yield from serialize_statement(content)
