from cxx.document.document import Document
from cxx.document_formatter.document_formatter import DocumentFormatter
from cxx.serialize.serialize_declaration import serialize_declaration


class MinifiedFormatter(DocumentFormatter):
    def format(self, document: Document) -> str:
        lines: list[str] = []

        if document.header:
            lines.append("#pragma once")

        for include in document.includes:
            open_bracket = "<" if include.system else '"'
            close_bracket = ">" if include.system else '"'
            lines.append(f"#include {open_bracket}{include.path}{close_bracket}")

        for declaration in document.declarations:
            lines.append(" ".join(serialize_declaration(declaration)))

        return "\n".join(lines)
