# Workbook — Chapter 2: Object-Oriented Programming (OOP) & Breaking the Monolith


---

## 2.1 OOP State & Dunders: Build a `DocumentStore` Class (`Foundation` · OOP)

Implement `@dataclass class Document(doc_id: str, text: str)` and `class DocumentStore` with:
- `add(doc: Document) -> None` (reject empty `doc.text.strip()` with `ValueError`)
- `get(doc_id: str) -> Document | None`
- `search(keyword: str) -> list[Document]` (case-insensitive substring match in `text`, preserving insertion order)
- `__len__(self) -> int` and `__contains__(self, doc_id: str) -> bool`

### Thinking Blueprint

- Block 1 (`Document` dataclass): Holds `doc_id` and `text`.
- Block 2 (`DocumentStore.__init__`): Initializes `self._docs: dict[str, Document] = {}` (Python 3.7+ dicts preserve insertion order!).
- Block 3 (Methods & Dunders): Implement `add`, `get`, `search`, `__len__`, and `__contains__`.

### Progressive Hints

1. Validate `if not doc.text.strip(): raise ValueError('Empty document')` inside `add()`.
2. In `__contains__`, return `doc_id in self._docs`.

### Dry-Run Trace
`store.add(Document('1', 'Hello AI'))` -> `len(store) == 1`, `'1' in store is True`, `store.search('ai')` returns `[Document('1', 'Hello AI')]`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** (1) `@dataclass` models passive record data; (2) `DocumentStore` encapsulates `_docs` behind validated methods (`add` guards empty text); (3) Dunder methods (`__len__`, `__contains__`) integrate naturally with Python syntax (`len(store)`, `'id' in store`).


---

## 2.2 OOP Composition & `__call__`: Composable Text Pipeline (`Intermediate` · OOP)

Implement three classes:
1. `StripWhitespace`: `__call__(self, text: str) -> str` collapses internal whitespace and strips ends.
2. `ReplaceWord(old: str, new: str)`: `__call__(self, text: str) -> str` replaces exact whitespace-separated words matching `old` with `new`.
3. `Pipeline(steps: list)`: `__call__(self, text: str) -> str` passes `text` sequentially through each step.

### Thinking Blueprint

- Each transform class holds its config in `__init__` and runs its action in `__call__`.
- `Pipeline` uses **composition** (`self.steps`)—it doesn't inherit from any transform, it simply calls each step in order.

### Progressive Hints

1. In `ReplaceWord`, split on whitespace (`text.split()`), swap `new if w == self.old else w`, and `' '.join(...)`.

### Dry-Run Trace
`Pipeline([StripWhitespace(), ReplaceWord('ml', 'AI')])('  hello   ml  ')` -> `'hello ml'` -> `'hello AI'`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** This is the exact *Composable Runnable* design pattern behind PyTorch `nn.Sequential` and LangChain LCEL (`step1 | step2`). Every stage implements the same `__call__(x) -> y` contract.


---

## 2.3 Pure Modular Log Line Parser (`Foundation` · OOP)

Write `parse_logs(lines: list[str]) -> dict[str, int]` counting `'INFO'`, `'WARN'`, `'ERROR'` from lines like `'[ERROR] Disk full'`, ignoring blank lines, missing brackets, or unknown levels.

### Thinking Blueprint

- Block 1: Pre-seed `counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}`.
- Block 2: Guard-clause loop extracts `[LEVEL]` cleanly.

### Progressive Hints

1. Check `if not s.startswith('[') or ']' not in s: continue`.

### Dry-Run Trace
`['[INFO] ok', 'junk', '[ERROR] x']` -> `{'INFO': 1, 'WARN': 0, 'ERROR': 1}`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** Pure function takes `list[str]` instead of a file path so it can be unit-tested in memory without touching disk.
