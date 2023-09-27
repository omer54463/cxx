from surgeon.declaration.declaration import Declaration
from surgeon.document.document import Document
from surgeon.document.document_include import DocumentInclude


def document(
    pragma_once: bool,
    includes: list[DocumentInclude] | None = None,
    declarations: list[Declaration] | None = None,
) -> Document:
    return Document(
        pragma_once,
        [] if includes is None else includes,
        [] if declarations is None else declarations,
    )
