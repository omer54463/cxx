from cxx.declaration.declaration import Declaration
from cxx.document.document import Document
from cxx.document.document_include import DocumentInclude


class Documents:
    def header(
        self,
        includes: list[DocumentInclude] | None = None,
        declarations: list[Declaration] | None = None,
    ) -> Document:
        return Document(
            pragma_once=True,
            includes=[] if includes is None else includes,
            declarations=[] if declarations is None else declarations,
        )

    def source(
        self,
        includes: list[DocumentInclude] | None = None,
        declarations: list[Declaration] | None = None,
    ) -> Document:
        return Document(
            pragma_once=False,
            includes=[] if includes is None else includes,
            declarations=[] if declarations is None else declarations,
        )
