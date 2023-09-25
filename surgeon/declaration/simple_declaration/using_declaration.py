from dataclasses import dataclass

from surgeon.declaration.simple_declaration.simple_declaration import SimpleDeclaration
from surgeon.declaration.simple_declaration.using_mode import UsingMode


@dataclass
class UsingDeclaration(SimpleDeclaration):
    mode: UsingMode
    identifier: str
