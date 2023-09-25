from surgeon.declaration.class_declaration.class_base import ClassBase
from surgeon.declaration.class_declaration.class_declaration import ClassDeclaration
from surgeon.declaration.class_declaration.class_declaration_block import (
    ClassDeclarationBlock,
)
from surgeon.declaration.class_declaration.class_definition import ClassDefinition
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.enum_declaration.enum_declaration import EnumDeclaration
from surgeon.declaration.enum_declaration.enum_definition import EnumDefinition
from surgeon.declaration.enum_declaration.enum_member import EnumMember
from surgeon.declaration.function_declaration.constructor_initializer import (
    ConstructorInitializer,
)
from surgeon.declaration.function_declaration.function_argument import FunctionArgument
from surgeon.declaration.function_declaration.function_declaration import (
    FunctionDeclaration,
)
from surgeon.declaration.function_declaration.function_definition import (
    FunctionDefinition,
)
from surgeon.declaration.namespace_declaration.namespace_declaration import (
    NamespaceDeclaration,
)
from surgeon.declaration.namespace_declaration.namespace_definition import (
    NamespaceDefinition,
)
from surgeon.declaration.simple_declaration.alias_declaration import (
    AliasDeclaration,
    AliasMode,
)
from surgeon.declaration.simple_declaration.static_assert_declaration import (
    StaticAssertDeclaration,
)
from surgeon.declaration.simple_declaration.using_declaration import (
    UsingDeclaration,
    UsingMode,
)
from surgeon.declaration.simple_declaration.variable_declaration import (
    VariableDeclaration,
)
from surgeon.expression.expression import Expression
from surgeon.statement.statement import Statement


class ClassDeclarations:
    def declaration(
        self,
        struct: bool,
        identifier: str,
        specifiers: list[str] | None = None,
    ) -> ClassDeclaration:
        return ClassDeclaration(
            [] if specifiers is None else specifiers,
            struct,
            identifier,
        )

    def definition(
        self,
        struct: bool,
        identifier: str,
        final: bool = False,
        bases: list[ClassBase] | None = None,
        declaration_blocks: list[ClassDeclarationBlock] | None = None,
        specifiers: list[str] | None = None,
    ) -> ClassDefinition:
        return ClassDefinition(
            [] if specifiers is None else specifiers,
            struct,
            identifier,
            final,
            [] if bases is None else bases,
            [] if declaration_blocks is None else declaration_blocks,
        )


class EnumDeclarations:
    def declaration(
        self,
        scoped: bool,
        identifier: str,
        specifiers: list[str] | None = None,
    ) -> EnumDeclaration:
        return EnumDeclaration(
            [] if specifiers is None else specifiers,
            scoped,
            identifier,
        )

    def definition(
        self,
        scoped: bool,
        identifier: str,
        specifiers: list[str] | None = None,
        members: list[EnumMember] | None = None,
    ) -> EnumDefinition:
        return EnumDefinition(
            [] if specifiers is None else specifiers,
            scoped,
            identifier,
            [] if members is None else members,
        )


class FunctionDeclarations:
    def declaration(
        self,
        return_type: str,
        identifier: str,
        arguments: list[FunctionArgument] | None = None,
        specifiers: list[str] | None = None,
    ) -> FunctionDeclaration:
        return FunctionDeclaration(
            [] if specifiers is None else specifiers,
            return_type,
            identifier,
            [] if arguments is None else arguments,
        )

    def definition(
        self,
        return_type: str,
        identifier: str,
        arguments: list[FunctionArgument] | None = None,
        initializers: list[ConstructorInitializer] | None = None,
        statements: list[Statement] | None = None,
        specifiers: list[str] | None = None,
    ) -> FunctionDefinition:
        return FunctionDefinition(
            [] if specifiers is None else specifiers,
            return_type,
            identifier,
            [] if arguments is None else arguments,
            [] if initializers is None else initializers,
            [] if statements is None else statements,
        )


class NamespaceDeclarations:
    def declaration(
        self,
        identifier: str,
        specifiers: list[str] | None = None,
    ) -> NamespaceDeclaration:
        return NamespaceDeclaration(
            [] if specifiers is None else specifiers,
            identifier,
        )

    def definition(
        self,
        identifier: str,
        declarations: list[Declaration] | None = None,
        specifiers: list[str] | None = None,
    ) -> NamespaceDefinition:
        return NamespaceDefinition(
            [] if specifiers is None else specifiers,
            identifier,
            [] if declarations is None else declarations,
        )


class Declarations:
    class_: ClassDeclarations
    enum: EnumDeclarations
    function: FunctionDeclarations
    namespace: NamespaceDeclarations

    def __init__(self) -> None:
        self.class_ = ClassDeclarations()
        self.enum = EnumDeclarations()
        self.function = FunctionDeclarations()
        self.namespace = NamespaceDeclarations()

    def alias(self, mode: AliasMode, old: str, new: str) -> AliasDeclaration:
        return AliasDeclaration(mode, old, new)

    def static_assert(
        self,
        expression: Expression,
        message: Expression,
    ) -> StaticAssertDeclaration:
        return StaticAssertDeclaration(expression, message)

    def variable(
        self,
        type: str,
        identifier: str,
        specifiers: list[str] | None = None,
        value: Expression | None = None,
    ) -> VariableDeclaration:
        return VariableDeclaration(
            [] if specifiers is None else specifiers,
            type,
            identifier,
            value,
        )

    def using(self, mode: UsingMode, identifier: str) -> UsingDeclaration:
        return UsingDeclaration(mode, identifier)
