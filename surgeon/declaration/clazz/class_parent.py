from dataclasses import dataclass

from surgeon.declaration.clazz.class_access import ClassAccess


@dataclass
class ClassParent:
    identifier: str
    access: ClassAccess = ClassAccess.DEFAULT
    virtual: bool = False
