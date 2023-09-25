import typing as t
from enum import Enum, auto

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
    @t.overload
    def create(
        self,
        literal_type: t.Literal[LiteralType.BOOLEAN],
        *,
        value: bool,
    ) -> BooleanLiteral:
        ...

    @t.overload
    def create(
        self,
        literal_type: t.Literal[LiteralType.CHARACTER],
        value: str,
    ) -> CharacterLiteral:
        ...

    @t.overload
    def create(
        self,
        literal_type: t.Literal[LiteralType.IDENTIFIER],
        value: str,
    ) -> IdentifierLiteral:
        ...

    @t.overload
    def create(
        self,
        literal_type: t.Literal[LiteralType.STRING],
        value: str,
    ) -> StringLiteral:
        ...

    @t.overload
    def create(
        self,
        literal_type: t.Literal[LiteralType.INTEGER],
        value: int,
        base: IntegerBase,
    ) -> IntegerLiteral:
        ...

    def create(
        self,
        literal_type: LiteralType,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> Literal:
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
