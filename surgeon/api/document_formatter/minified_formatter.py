from surgeon.api.document.document import Document
from surgeon.api.document_formatter.document_formatter import DocumentFormatter
from surgeon.serialize.serialize_declaration import serialize_declaration


class MinifiedFormatter(DocumentFormatter):
    def format(self, document: Document) -> str:
        lines: list[str] = []

        if document.pragma_once:
            lines.append("#pragma once")

        for include in document.includes:
            open_bracket = "<" if include.system else '"'
            close_bracket = ">" if include.system else '"'
            lines.append(f"#include {open_bracket}{include.path}{close_bracket}")

        for declaration in document.declarations:
            lines.append(" ".join(serialize_declaration(declaration)))

        return "\n".join(lines)
