from collections.abc import Iterator


def flatten_lines(lines: list[list[str]]) -> Iterator[str]:
    yield from (word for line in lines for word in line)
