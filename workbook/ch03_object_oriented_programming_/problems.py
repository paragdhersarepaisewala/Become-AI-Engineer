"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 3.1: First Class & Methods: Build a `BankAccount` ---
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # TODO: save owner and balance on self
        pass

    def deposit(self, amount: float) -> None:
        pass

    def withdraw(self, amount: float) -> bool:
        pass

if __name__ == '__main__':
    acc = BankAccount('Sara', 100.0)
    acc.deposit(50.0)
    print(acc.owner, acc.balance)


# --- 3.2: Composition & `@dataclass`: `Song` + `Playlist` ---
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    seconds: int

class Playlist:
    def __init__(self) -> None:
        # TODO
        pass

    def add(self, song: Song) -> None:
        pass

    def total_seconds(self) -> int:
        pass

    def __len__(self) -> int:
        pass


# --- 3.3: Callable Objects (`__call__`): Composable Text Pipeline ---
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
