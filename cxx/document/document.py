from dataclasses import dataclass

from cxx.declaration.declaration import Declaration


@dataclass
class Document:
    header: bool
    includes: list[str]
    declarations: list[Declaration]
