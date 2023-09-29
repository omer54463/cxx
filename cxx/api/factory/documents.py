from cxx.declaration.declaration import Declaration
from cxx.document.document import Document


class Documents:
    def header(
        self,
        includes: list[str] | None = None,
        declarations: list[Declaration] | None = None,
    ) -> Document:
        return Document(
            header=True,
            includes=[] if includes is None else includes,
            declarations=[] if declarations is None else declarations,
        )

    def source(
        self,
        includes: list[str] | None = None,
        declarations: list[Declaration] | None = None,
    ) -> Document:
        return Document(
            header=False,
            includes=[] if includes is None else includes,
            declarations=[] if declarations is None else declarations,
        )
