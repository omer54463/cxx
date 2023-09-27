from abc import ABC, abstractmethod

from cxx.document.document import Document


class DocumentFormatter(ABC):
    @abstractmethod
    def format(self, document: Document) -> str:
        ...
