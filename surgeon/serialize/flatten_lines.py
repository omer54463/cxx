from collections.abc import Iterable


def flatten_lines(lines: Iterable[Iterable[str]]) -> Iterable[str]:
    yield from (word for words in lines for word in words)
