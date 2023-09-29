from __future__ import annotations

from typing import TYPE_CHECKING

from cxx.document.document import Document
from cxx.document.document_include import DocumentInclude

if TYPE_CHECKING:
    from cxx.declaration.declaration import Declaration


class DocumentBuilder:
    header: bool
    includes: list[DocumentInclude]
    declarations: list[Declaration]

    def __init__(self, header: bool = False) -> None:
        self.header = header
        self.includes = []
        self.declarations = []

    def add_include(self, path: str, system: bool = False) -> DocumentBuilder:
        self.includes.append(DocumentInclude(path, system))
        return self

    def add_declaration(self, declaration: Declaration) -> DocumentBuilder:
        self.declarations.append(declaration)
        return self

    def build(self) -> Document:
        return Document(self.header, self.includes, self.declarations)
