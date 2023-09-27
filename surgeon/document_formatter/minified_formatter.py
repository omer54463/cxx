from surgeon.document.document import Document
from surgeon.document_formatter.document_formatter import DocumentFormatter
from surgeon.serialize.serialize_declaration import serialize_declaration


class MinifiedFormatter(DocumentFormatter):
    line_breaks: bool

    def __init__(self, line_breaks: bool = False) -> None:
        self.line_breaks = line_breaks

    def format(self, document: Document) -> str:
        lines: list[str] = []

        if document.pragma_once:
            lines.append("#pragma once")
            self._add_line_break(lines)

        for include in document.includes:
            open_bracket = "<" if include.system else '"'
            close_bracket = ">" if include.system else '"'
            lines.append(f"#include {open_bracket}{include.path}{close_bracket}")
        self._add_line_break(lines)

        for declaration in document.declarations:
            lines.append(" ".join(serialize_declaration(declaration)))
            self._add_line_break(lines)

        return "\n".join(lines)

    def _add_line_break(self, lines: list[str]) -> None:
        if self.line_breaks:
            lines.append("")
