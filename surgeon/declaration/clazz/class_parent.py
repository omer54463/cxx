from dataclasses import dataclass

from surgeon.declaration.clazz.class_access import ClassAccess


@dataclass
class ClassParent:
    name: str
    access: ClassAccess = ClassAccess.NONE
