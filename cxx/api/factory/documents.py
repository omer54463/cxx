from cxx.declaration.declaration import Declaration
from cxx.document.document import Document
from cxx.document.document_include import DocumentInclude


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
