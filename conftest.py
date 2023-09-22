from pkgutil import iter_modules

from surgeon.tests.unit import mocks

pytest_plugins = [
    f"{mocks.__name__}.{info.name}" for info in iter_modules(mocks.__path__)
]
