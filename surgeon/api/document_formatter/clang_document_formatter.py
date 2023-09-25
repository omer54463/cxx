from pathlib import Path
from shutil import copy
from subprocess import check_output
from tempfile import TemporaryDirectory

from surgeon.api.document.document import Document
from surgeon.api.document_formatter.document_formatter import DocumentFormatter
from surgeon.api.document_formatter.minified_document_formatter import (
    MinifiedDocumentFormatter,
)


class ClangDocumentFormatter(DocumentFormatter):
    executable_path: Path
    configuration_path: Path | None
    minified_formatter: MinifiedDocumentFormatter

    def __init__(
        self,
        executable_path: Path = Path("clang-format"),
        configuration_path: Path | None = None,
    ) -> None:
        self.executable_path = executable_path
        self.configuration_path = configuration_path
        self.minified_formatter = MinifiedDocumentFormatter()

    def format(self, document: Document) -> str:
        minified = self.minified_formatter.format(document)

        with TemporaryDirectory() as temporary_directory:
            if self.configuration_path is not None:
                copy(str(self.configuration_path), temporary_directory)

            temporary_file_path = Path(temporary_directory) / "source"
            with temporary_file_path.open("w") as temporary_file:
                temporary_file.write(minified)

            arguments = [str(self.executable_path), temporary_file.name]
            result_bytes = check_output(arguments)

        return result_bytes.decode()
