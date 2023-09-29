from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory

from cxx.document.document import Document
from cxx.document_formatter.document_formatter import DocumentFormatter
from cxx.document_formatter.minified_formatter import (
    MinifiedFormatter,
)


class ClangFormatter(DocumentFormatter):
    executable_path: Path
    configuration_path: Path | None
    configuration_style: str | None
    underlying_formatter: DocumentFormatter

    def __init__(
        self,
        executable_path: Path = Path("clang-format"),
        configuration_path: Path | None = None,
        configuration_style: str | None = None,
        underlying_formatter: DocumentFormatter | None = None,
    ) -> None:
        self.executable_path = executable_path
        self.configuration_path = configuration_path
        self.configuration_style = configuration_style
        self.underlying_formatter = (
            MinifiedFormatter()
            if underlying_formatter is None
            else underlying_formatter
        )

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

        configuration_path.write_text(configuration)
        return temporary_directory_path

    def _setup_source(self, temporary_directory_path: Path, document: Document) -> Path:
        temporary_file_path = temporary_directory_path / "source"

        minified = self.underlying_formatter.format(document)
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
        return result_bytes.replace(b"\r", b"").decode()
