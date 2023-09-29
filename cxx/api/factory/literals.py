from cxx.expression.literal.boolean_literal import BooleanLiteral
from cxx.expression.literal.character_literal import CharacterLiteral
from cxx.expression.literal.identifier_literal import IdentifierLiteral
from cxx.expression.literal.integer_literal import IntegerBase, IntegerLiteral
from cxx.expression.literal.string_literal import StringLiteral


class Literals:
    def boolean(self, value: bool) -> BooleanLiteral:
        return BooleanLiteral(value)

    def character(self, value: str) -> CharacterLiteral:
        return CharacterLiteral(value)

    def identifier(self, identifier: str) -> IdentifierLiteral:
        return IdentifierLiteral(identifier)

    def integer(
        self,
        value: int,
        base: IntegerBase = IntegerBase.DECIMAL,
    ) -> IntegerLiteral:
        return IntegerLiteral(value, base)

    def string(self, value: str, wide: bool = False) -> StringLiteral:
        return StringLiteral(value, wide)
