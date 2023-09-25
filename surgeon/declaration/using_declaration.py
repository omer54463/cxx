from dataclasses import dataclass

from surgeon.declaration.declaration import Declaration
from surgeon.declaration.using_mode import UsingMode


@dataclass
class UsingDeclaration(Declaration):
    mode: UsingMode
    identifier: str
