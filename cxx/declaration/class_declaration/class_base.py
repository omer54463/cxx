from dataclasses import dataclass

from cxx.declaration.class_declaration.class_access import ClassAccess


@dataclass
class ClassBase:
    virtual: bool
    access: ClassAccess | None
    identifier: str
