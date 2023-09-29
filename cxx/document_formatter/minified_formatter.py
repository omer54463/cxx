from cxx.document.document import Document
from cxx.document_formatter.document_formatter import DocumentFormatter
from cxx.serialize.serialize_declaration import serialize_declaration


class MinifiedFormatter(DocumentFormatter):
    def format(self, document: Document) -> str:
        lines: list[str] = []

        if document.header:
            lines.append("#pragma once")

        for include in document.includes:
            if (include.startswith("<") and include.endswith(">")) or (
                include.startswith('"') and include.endswith('"')
            ):
                actual_include = include
            else:
                actual_include = f'"{include}"'
            lines.append(f"#include {actual_include}")

        for declaration in document.declarations:
            lines.append(" ".join(serialize_declaration(declaration)))

        return "\n".join(lines)
