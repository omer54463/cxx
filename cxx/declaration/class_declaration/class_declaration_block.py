from dataclasses import dataclass

from cxx.declaration.class_declaration.class_access import ClassAccess
from cxx.declaration.declaration import Declaration


@dataclass
class ClassDeclarationBlock:
    access: ClassAccess | None
    declarations: list[Declaration]
