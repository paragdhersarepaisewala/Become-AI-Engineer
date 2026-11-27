"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 2.1: OOP State & Dunders: Build a `DocumentStore` Class ---
from dataclasses import dataclass

@dataclass
class Document:
    doc_id: str
    text: str

class DocumentStore:
    def __init__(self) -> None:
        # TODO: initialize internal storage
        pass

    def add(self, doc: Document) -> None:
        pass

    def get(self, doc_id: str) -> Document | None:
        pass

    def search(self, keyword: str) -> list[Document]:
        pass

    def __len__(self) -> int:
        pass

    def __contains__(self, doc_id: str) -> bool:
        pass


# --- 2.2: OOP Composition & `__call__`: Composable Text Pipeline ---
class StripWhitespace:
    def __call__(self, text: str) -> str:
        pass

class ReplaceWord:
    def __init__(self, old: str, new: str) -> None:
        pass

    def __call__(self, text: str) -> str:
        pass

class Pipeline:
    def __init__(self, steps: list) -> None:
        pass

    def __call__(self, text: str) -> str:
        pass


# --- 2.3: Pure Modular Log Line Parser ---
def parse_logs(lines: list[str]) -> dict[str, int]:
    # TODO: count INFO, WARN, ERROR ignoring invalid lines
    pass
