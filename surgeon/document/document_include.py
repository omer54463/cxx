from dataclasses import dataclass


@dataclass
class DocumentInclude:
    path: str
    system: bool
