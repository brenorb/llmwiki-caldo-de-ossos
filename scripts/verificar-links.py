#!/usr/bin/env python3
"""Verifica destinos Markdown locais e páginas alcançáveis a partir do índice."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)")
FENCE = re.compile(r"^```.*?^```[ \t]*$", flags=re.MULTILINE | re.DOTALL)
HEADING = re.compile(r"^#{1,6} +(.+?)\s*#*\s*$", flags=re.MULTILINE)


def anchors(markdown):
    used = set()
    for title in HEADING.findall(markdown):
        slug = re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")
        anchor = slug
        occurrence = 1
        while anchor in used:
            anchor = f"{slug}-{occurrence}"
            occurrence += 1
        used.add(anchor)
    return used


def main():
    documents = {
        path: FENCE.sub("", path.read_text(encoding="utf-8"))
        for path in sorted(ROOT.rglob("*.md"))
    }
    graph = {path: set() for path in documents}
    failures = []
    count = 0
    for source, markdown in documents.items():
        for target in LINK.findall(markdown):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            count += 1
            path = (source.parent / unquote(url.path)).resolve() if url.path else source
            if not path.is_relative_to(ROOT) or not path.is_file():
                failures.append(f"{source.relative_to(ROOT)} → {target}")
                continue
            if path in documents:
                graph[source].add(path)
                if url.fragment and unquote(url.fragment) not in anchors(documents[path]):
                    failures.append(f"{source.relative_to(ROOT)} → âncora ausente: {target}")

    visited = set()
    pending = [ROOT / "index.md"]
    while pending:
        path = pending.pop()
        if path not in visited:
            visited.add(path)
            pending.extend(graph.get(path, ()))

    for path in sorted(documents.keys() - visited):
        failures.append(f"Página não alcançada pelo índice: {path.relative_to(ROOT)}")
    for failure in failures:
        print(failure, file=sys.stderr)
    print(f"{len(documents)} arquivos Markdown, {count} links locais, {len(failures)} problemas.")
    return bool(failures)


if __name__ == "__main__":
    sys.exit(main())
