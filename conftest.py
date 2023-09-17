from pkgutil import iter_modules
from re import compile

from surgeon.tests.unit import mocks

MOCK_FILE_REGEX = compile(r"^mock_.*")

pytest_plugins = [
    f"{mocks.__name__}.{info.name}"
    for info in iter_modules(mocks.__path__)
    if MOCK_FILE_REGEX.match(info.name)
]
