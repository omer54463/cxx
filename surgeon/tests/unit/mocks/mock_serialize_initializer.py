from collections.abc import Iterable
from dataclasses import dataclass
from types import ModuleType

import pytest
import pytest_mock

from surgeon.initializer.initializer import Initializer


@dataclass
class FakeInitializer(Initializer):
    content: str


def fake_serialize_initializer(initializer: Initializer) -> Iterable[str]:
    assert isinstance(initializer, FakeInitializer), "Invalid initializer type in test"
    yield initializer.content


@pytest.fixture()
def mock_serialize_initializer(
    serialization_modules: Iterable[ModuleType],
    module_mocker: pytest_mock.MockerFixture,
) -> None:
    for module in serialization_modules:
        if not hasattr(module, "serialize_initializer"):
            continue

        module_mocker.patch.object(
            module,
            "serialize_initializer",
            wraps=fake_serialize_initializer,
        )
