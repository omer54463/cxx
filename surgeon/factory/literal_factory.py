from enum import Enum, auto
from typing import Any, overload
from typing import Literal as Ll

from surgeon.expression.literal.boolean_literal import BooleanLiteral
from surgeon.expression.literal.character_literal import CharacterLiteral
from surgeon.expression.literal.identifier_literal import IdentifierLiteral
from surgeon.expression.literal.integer_base import IntegerBase
from surgeon.expression.literal.integer_literal import IntegerLiteral
from surgeon.expression.literal.literal import Literal
from surgeon.expression.literal.string_literal import StringLiteral


class LiteralType(Enum):
    BOOLEAN = auto()
    CHARACTER = auto()
    IDENTIFIER = auto()
    INTEGER = auto()
    STRING = auto()


class LiteralFactory:
    @overload
    def create(self, literal_type: Ll[LiteralType.BOOLEAN], *, value: bool) -> Literal:
        ...

    @overload
    def create(self, literal_type: Ll[LiteralType.CHARACTER], value: str) -> Literal:
        ...

    @overload
    def create(self, literal_type: Ll[LiteralType.IDENTIFIER], value: str) -> Literal:
        ...

    @overload
    def create(self, literal_type: Ll[LiteralType.STRING], value: str) -> Literal:
        ...

    @overload
    def create(
        self,
        literal_type: Ll[LiteralType.INTEGER],
        value: int,
        base: IntegerBase,
    ) -> Literal:
        ...

    def create(self, literal_type: LiteralType, *args: Any, **kwargs: Any) -> Literal:
        match literal_type:
            case LiteralType.BOOLEAN:
                return BooleanLiteral(*args, **kwargs)

            case LiteralType.CHARACTER:
                return CharacterLiteral(*args, **kwargs)

            case LiteralType.IDENTIFIER:
                return IdentifierLiteral(*args, **kwargs)

            case LiteralType.INTEGER:
                return IntegerLiteral(*args, **kwargs)

            case LiteralType.STRING:
                return StringLiteral(*args, **kwargs)

        raise TypeError(f"Invalid literal type {literal_type}")
