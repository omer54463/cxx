from collections.abc import Iterable

from surgeon.initializer.initializer import Initializer


def serialize_initializer(initializer: Initializer) -> Iterable[str]:
    match initializer:
        case _:
            raise TypeError(f"Unexpected type {type(initializer)}")


def serialize_optional_initializer(initializer: Initializer | None) -> Iterable[str]:
    if initializer is not None:
        yield from serialize_initializer(initializer)
