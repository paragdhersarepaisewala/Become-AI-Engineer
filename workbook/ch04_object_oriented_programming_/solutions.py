"""Reference solutions with explanations."""


# --- 4.1: First Class & Methods: Build a `BankAccount` ---
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

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
        self.songs: list[Song] = []

    def add(self, song: Song) -> None:
        self.songs.append(song)

    def total_seconds(self) -> int:
        return sum(s.seconds for s in self.songs)

    def __len__(self) -> int:
        return len(self.songs)


# --- 4.3: Callable Objects (`__call__`): Composable Text Pipeline ---
class StripWhitespace:
    def __call__(self, text: str) -> str:
        return ' '.join(text.split())

class ReplaceWord:
    def __init__(self, old: str, new: str) -> None:
        self.old = old
        self.new = new

    def __call__(self, text: str) -> str:
        words = []
        for w in text.split():
            if w == self.old:
                words.append(self.new)
            else:
                words.append(w)
        return ' '.join(words)

class Pipeline:
    def __init__(self, steps: list) -> None:
        self.steps = list(steps)

    def __call__(self, text: str) -> str:
        out = text
        for step in self.steps:
            out = step(out)
        return out
