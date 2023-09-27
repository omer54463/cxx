from __future__ import annotations

from typing import TYPE_CHECKING

from surgeon.document.document import Document
from surgeon.document.document_include import DocumentInclude

if TYPE_CHECKING:
    from surgeon.declaration.declaration import Declaration


class DocumentBuilder:
    pragma_once: bool
    includes: list[DocumentInclude]
    declarations: list[Declaration]

    def __init__(self, pragma_once: bool = False) -> None:
        self.pragma_once = pragma_once
        self.includes = []
        self.declarations = []

    def add_include(self, path: str, system: bool = False) -> DocumentBuilder:
        self.includes.append(DocumentInclude(path, system))
        return self

    def add_declaration(self, declaration: Declaration) -> DocumentBuilder:
        self.declarations.append(declaration)
        return self

    def build(self) -> Document:
        return Document(self.pragma_once, self.includes, self.declarations)
