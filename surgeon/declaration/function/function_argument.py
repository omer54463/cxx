from dataclasses import dataclass

from surgeon.initializer.initializer import Initializer


@dataclass
class FunctionArgument:
    type: str
    identifier: str
    default: Initializer
