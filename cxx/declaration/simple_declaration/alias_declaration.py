from dataclasses import dataclass
from enum import Enum, auto

from cxx.declaration.simple_declaration.simple_declaration import SimpleDeclaration


class AliasMode(Enum):
    DEFAULT = auto()
    NAMESPACE = auto()
    TYPE_DEF = auto()


@dataclass
class AliasDeclaration(SimpleDeclaration):
    mode: AliasMode
    old_identifier: str
    new_identifier: str
