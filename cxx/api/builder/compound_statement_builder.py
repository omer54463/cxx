from __future__ import annotations

from typing import TYPE_CHECKING

from cxx.statement.compound_statement import CompountStatement

if TYPE_CHECKING:
    from cxx.statement.statement import Statement


class CompoundStatementBuilder:
    statements: list[Statement]

    def __init__(self) -> None:
        self.statements = []

    def add_statement(self, statement: Statement) -> CompoundStatementBuilder:
        self.statements.append(statement)
        return self

    def build(self) -> CompountStatement:
        return CompountStatement(self.statements)
