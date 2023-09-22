from dataclasses import dataclass, field

from surgeon.declaration.clazz.class_access import ClassAccess
from surgeon.declaration.declaration import Declaration


@dataclass
class ClassDeclarationBlock:
    access: ClassAccess
    declarations: list[Declaration] = field(default_factory=list)
