from pathlib import Path
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
    configuration_style: str | None
    minified_formatter: MinifiedDocumentFormatter

    def __init__(
        self,
        executable_path: Path = Path("clang-format"),
        configuration_path: Path | None = None,
        configuration_style: str | None = None,
    ) -> None:
        self.executable_path = executable_path
        self.configuration_path = configuration_path
        self.configuration_style = configuration_style
        self.minified_formatter = MinifiedDocumentFormatter()

    def format(self, document: Document) -> str:
        with TemporaryDirectory() as temporary_directory:
            directory_path = Path(temporary_directory)

            self._setup_configuration(directory_path)
            source_path = self._setup_source(directory_path, document)
            return self._format(directory_path, source_path)

    def _setup_configuration(self, temporary_directory_path: Path) -> Path:
        configuration_path = temporary_directory_path / ".clang-format"

        if self.configuration_path is not None:
            configuration = self.configuration_path.read_text()

        else:
            configuration_style = (
                "llvm" if self.configuration_style is None else self.configuration_style
            )

            arguments = [
                str(self.executable_path),
                f"-style={configuration_style}",
                "-dump-config",
            ]
            configuration = check_output(arguments).decode()
            configuration_path.write_text(configuration, encoding="ascii")

        return temporary_directory_path

    def _setup_source(self, temporary_directory_path: Path, document: Document) -> Path:
        temporary_file_path = temporary_directory_path / "source"

        minified = self.minified_formatter.format(document)
        with temporary_file_path.open("w") as temporary_file:
            temporary_file.write(minified)

        return temporary_file_path

    def _format(
        self,
        temporary_directory_path: Path,
        temporary_source_path: Path,
    ) -> str:
        arguments = [str(self.executable_path), str(temporary_source_path)]
        result_bytes = check_output(arguments, cwd=str(temporary_directory_path))
        return result_bytes.decode()
