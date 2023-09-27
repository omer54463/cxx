from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.document.document_include import DocumentInclude


@dataclass
class Document:
    pragma_once: bool
    includes: list[DocumentInclude]
    declarations: list[Declaration]
