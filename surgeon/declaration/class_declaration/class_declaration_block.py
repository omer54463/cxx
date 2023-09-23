from dataclasses import dataclass

from surgeon.declaration.class_declaration.class_access import ClassAccess
from surgeon.declaration.declaration import Declaration


@dataclass
class ClassDeclarationBlock:
    access: ClassAccess | None
    declarations: list[Declaration]
