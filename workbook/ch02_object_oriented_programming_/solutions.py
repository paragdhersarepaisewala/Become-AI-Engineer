"""Reference solutions with explanations."""


# --- 2.1: OOP State & Dunders: Build a `DocumentStore` Class ---
from dataclasses import dataclass

@dataclass
class Document:
    doc_id: str
    text: str

class DocumentStore:
    def __init__(self) -> None:
        self._docs: dict[str, Document] = {}

    def add(self, doc: Document) -> None:
        if not doc.text.strip():
            raise ValueError('Document text cannot be empty')
        self._docs[doc.doc_id] = doc

    def get(self, doc_id: str) -> Document | None:
        return self._docs.get(doc_id)

    def search(self, keyword: str) -> list[Document]:
        q = keyword.lower()
        return [d for d in self._docs.values() if q in d.text.lower()]

    def __len__(self) -> int:
        return len(self._docs)

    def __contains__(self, doc_id: str) -> bool:
        return doc_id in self._docs


# --- 2.2: OOP Composition & `__call__`: Composable Text Pipeline ---
class StripWhitespace:
    def __call__(self, text: str) -> str:
        return ' '.join(text.split())

class ReplaceWord:
    def __init__(self, old: str, new: str) -> None:
        self.old = old
        self.new = new

    def __call__(self, text: str) -> str:
        return ' '.join(self.new if w == self.old else w for w in text.split())

class Pipeline:
    def __init__(self, steps: list) -> None:
        self.steps = list(steps)

    def __call__(self, text: str) -> str:
        out = text
        for step in self.steps:
            out = step(out)
        return out


# --- 2.3: Pure Modular Log Line Parser ---
def parse_logs(lines: list[str]) -> dict[str, int]:
    counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}
    for line in lines:
        s = line.strip()
        if not s.startswith('[') or ']' not in s:
            continue
        level = s[1:s.index(']')].upper()
        if level in counts:
            counts[level] += 1
    return counts
