from dataclasses import dataclass

from surgeon.initializer.initializer import Initializer


@dataclass
class ConstructorInitializer:
    identifier: str
    initializer: Initializer
