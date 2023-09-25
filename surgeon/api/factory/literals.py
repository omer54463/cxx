from surgeon.expression.literal.boolean_literal import BooleanLiteral
from surgeon.expression.literal.character_literal import CharacterLiteral
from surgeon.expression.literal.identifier_literal import IdentifierLiteral
from surgeon.expression.literal.integer_literal import IntegerBase, IntegerLiteral
from surgeon.expression.literal.string_literal import StringLiteral


class Literals:
    def boolean(self, value: bool) -> BooleanLiteral:
        return BooleanLiteral(value)

    def character(self, value: str) -> CharacterLiteral:
        return CharacterLiteral(value)

    def identifier(self, identifier: str) -> IdentifierLiteral:
        return IdentifierLiteral(identifier)

    def integer(self, value: int, base: IntegerBase) -> IntegerLiteral:
        return IntegerLiteral(value, base)

    def string(self, value: str) -> StringLiteral:
        return StringLiteral(value)
