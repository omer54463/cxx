from dataclasses import dataclass
from enum import Enum, auto

from cxx.declaration.simple_declaration.simple_declaration import SimpleDeclaration


class UsingMode(Enum):
    DEFAULT = auto()
    ENUM = auto()
    NAMESPACE = auto()


@dataclass
class UsingDeclaration(SimpleDeclaration):
    mode: UsingMode
    identifier: str
