from collections.abc import Iterable

from surgeon.declaration.declaration import Declaration


def serialize_declaration(_declaration: Declaration) -> Iterable[str]:
    raise NotImplementedError("TODO")


def serialize_optional_declaration(declaration: Declaration | None) -> Iterable[str]:
    if declaration is not None:
        yield from serialize_declaration(declaration)
