from abc import ABC, abstractmethod

from surgeon.document.document import Document


class DocumentFormatter(ABC):
    @abstractmethod
    def format(self, document: Document) -> str:
        ...
