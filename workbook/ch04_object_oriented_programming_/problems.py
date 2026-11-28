"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 4.1: First Class & Methods: Build a `BankAccount` ---
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        pass

    def deposit(self, amount: float) -> None:
        pass

    def withdraw(self, amount: float) -> bool:
        pass

if __name__ == '__main__':
    acc = BankAccount('Sara', 100.0)
    acc.deposit(50.0)
    print(acc.owner, acc.balance)


# --- 4.2: Composition & `@dataclass`: `Song` + `Playlist` ---
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    seconds: int

class Playlist:
    def __init__(self) -> None:
        pass

    def add(self, song: Song) -> None:
        pass

    def total_seconds(self) -> int:
        pass

    def __len__(self) -> int:
        pass
