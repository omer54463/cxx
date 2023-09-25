from abc import ABC, abstractmethod

from surgeon.api.document.document import Document


class DocumentFormatter(ABC):
    @abstractmethod
    def format(self, document: Document) -> str:
        ...
