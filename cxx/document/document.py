from dataclasses import dataclass

from cxx.declaration.declaration import Declaration
from cxx.document.document_include import DocumentInclude


@dataclass
class Document:
    header: bool
    includes: list[DocumentInclude]
    declarations: list[Declaration]
