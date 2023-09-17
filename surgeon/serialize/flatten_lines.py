from collections.abc import Iterable


def flatten_lines(lines: Iterable[Iterable[str]]) -> Iterable[str]:
    yield from (word for line in lines for word in line)
