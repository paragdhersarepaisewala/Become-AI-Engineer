# Workbook — Chapter 4: Object-Oriented Programming (OOP) From Ground Zero


---

## 4.1 First Class & Methods: Build a `BankAccount` (`Foundation` · OOP)

Build `BankAccount(owner, balance=0.0)` with `deposit(amount)` (`ValueError` if `<=0`) and `withdraw(amount) -> bool`.

### Thinking Blueprint

- Save `self.owner` and `self.balance` in `__init__`.
- Guard `<= 0` amounts.

### Progressive Hints

1. Always put `self` as the first parameter of every method.

### Dry-Run Trace
`a = BankAccount('Sara', 100); a.deposit(50)` -> `150`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** `self` isolates each account's balance, and methods validate state changes.


---

## 4.2 Composition & `@dataclass`: `Song` + `Playlist` (`Foundation` · OOP)

Implement `@dataclass class Song(title: str, seconds: int)` and `class Playlist` with `add(song)`, `total_seconds() -> int`, and `__len__() -> int`.

### Thinking Blueprint

- `Playlist.__init__` sets `self.songs = []`.

### Progressive Hints

1. `return sum(s.seconds for s in self.songs)`

### Dry-Run Trace
`Intro (90s) + Main (210s)` -> `len == 2`, `total_seconds == 300`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** Composition (`Playlist` holding `Song` objects) keeps each class small.


---

## 4.3 Callable Objects (`__call__`): Composable Text Pipeline (`Intermediate` · OOP)

Implement `StripWhitespace`, `ReplaceWord(old, new)`, and `Pipeline(steps)` where each has `__call__(self, text: str) -> str`.

### Thinking Blueprint

- Each step holds config in `__init__` and runs in `__call__`.

### Progressive Hints

1. `' '.join(text.split())` collapses extra whitespace cleanly.

### Dry-Run Trace
`Pipeline([StripWhitespace(), ReplaceWord('ml', 'AI')])('  learn   ml ')` -> `'learn AI'`.

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
```

**High-Level Blocks:** Uniform `__call__` interfaces plug together just like PyTorch `nn.Sequential` and LangChain LCEL.
