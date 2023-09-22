from dataclasses import dataclass, field

from surgeon.declaration.clazz.class_access import ClassAccess
from surgeon.declaration.clazz.class_parent import ClassParent
from surgeon.declaration.declaration import Declaration
from surgeon.declaration.specifier import Specifier


@dataclass
class ClassDefinition(Declaration):
    name: str
    declarations: list[Declaration | ClassAccess] = field(default_factory=list)
    final: bool = False
    parents: list[ClassParent] = field(default_factory=list)
    specifiers: Specifier = Specifier.NONE
