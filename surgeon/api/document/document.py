from dataclasses import dataclass

from surgeon.api.document.document_include import DocumentInclude
from surgeon.declaration.declaration import Declaration


@dataclass
class Document:
    pragma_once: bool
    includes: list[DocumentInclude]
    declarations: list[Declaration]
