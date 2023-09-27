from cxx.declaration.declaration import Declaration
from cxx.expression.expression import Expression
from cxx.statement.compound_statement import CompountStatement
from cxx.statement.declaration_statement import DeclarationStatement
from cxx.statement.expression_statement import ExpressionStatement
from cxx.statement.iteration_statement.do_while_statement import DoWhileStatement
from cxx.statement.iteration_statement.for_statement import ForStatement
from cxx.statement.iteration_statement.while_statement import WhileStatement
from cxx.statement.jump_statement.break_statement import BreakStatement
from cxx.statement.jump_statement.continue_statement import ContinueStatement
from cxx.statement.jump_statement.goto_statement import GotoStatement
from cxx.statement.jump_statement.return_statement import ReturnStatement
from cxx.statement.labeled_statement.case_statement import CaseStatement
from cxx.statement.labeled_statement.default_statement import DefaultStatement
from cxx.statement.labeled_statement.label_statement import LabelStatement
from cxx.statement.null_statement import NullStatement
from cxx.statement.selection_statement.if_statement import IfStatement
from cxx.statement.selection_statement.switch_statement import SwitchStatement
from cxx.statement.statement import Statement


class Statements:
    def null(self) -> NullStatement:
        return NullStatement()

    def expression(self, content: Expression) -> ExpressionStatement:
        return ExpressionStatement(content)

    def declaration(self, content: Declaration) -> DeclarationStatement:
        return DeclarationStatement(content)

    def compound(self, content: list[Statement] | None) -> CompountStatement:
        return CompountStatement([] if content is None else content)

    def if_(
        self,
        condition: Expression,
        content: Statement,
        else_content: Statement | None = None,
        initializer: Statement | None = None,
        constexpr: bool = False,
    ) -> IfStatement:
        return IfStatement(constexpr, initializer, condition, content, else_content)

    def switch(
        self,
        value: Expression,
        content: Statement,
        initializer: Statement | None = None,
    ) -> SwitchStatement:
        return SwitchStatement(initializer, value, content)

    def label(self, identifier: str) -> LabelStatement:
        return LabelStatement(identifier)

    def default(self) -> DefaultStatement:
        return DefaultStatement()

    def case(self, value: Expression) -> CaseStatement:
        return CaseStatement(value)

    def break_(self) -> BreakStatement:
        return BreakStatement()

    def continue_(self) -> ContinueStatement:
        return ContinueStatement()

    def goto(self, identifier: str) -> GotoStatement:
        return GotoStatement(identifier)

    def return_(self, value: Expression | None = None) -> ReturnStatement:
        return ReturnStatement(value)

    def do_while(self, content: Statement, condition: Expression) -> DoWhileStatement:
        return DoWhileStatement(content, condition)

    def for_(
        self,
        initializer: Statement,
        content: Statement,
        condition: Expression | None = None,
        progression: Expression | None = None,
    ) -> ForStatement:
        return ForStatement(initializer, condition, progression, content)

    def while_(self, condition: Expression, content: Statement) -> WhileStatement:
        return WhileStatement(condition, content)
