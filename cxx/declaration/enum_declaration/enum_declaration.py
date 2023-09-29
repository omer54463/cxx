from dataclasses import dataclass

from cxx.declaration.declaration import Declaration


@dataclass
class EnumDeclaration(Declaration):
    specifiers: list[str]
    scoped: bool
    identifier: str
    underlying_type: str | None
