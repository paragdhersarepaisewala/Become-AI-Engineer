# Chapter 4: Object-Oriented Programming (OOP) From Ground Zero

*Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, composition, and splitting files.*

**Why It Matters:** Pydantic models, PyTorch `nn.Module`, FastAPI dependencies, and LangChain Runnables are all built with OOP classes. Learning classes slowly from first principles makes every library in Phase 2–4 feel natural.

**Skills Covered:** Why Classes?, __init__ & self, Methods, __repr__ & @dataclass, Composition, Modules & pytest


---

## 4.1 Why Do Classes Exist? (Solving the Loose-Variables Mess)

> **Before You Start:** Forget textbook jargon like 'polymorphism' for now. Start with the exact everyday problem a `class` solves.

### 1. Definition
A **class** is a blueprint that bundles an item's **data (attributes)** and its **actions (methods)** together into one neat **object**.

### 2. Exact Syntax — Before OOP (Messy) vs With a Class (Clean)
```python
# WITHOUT OOP (messy as soon as you have 5 accounts!):
acc1_owner = 'Sara'
acc1_balance = 100

# WITH OOP (1 blueprint -> create as many objects as you want):
class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance
```

- Think of `class` as a cookie cutter, and `BankAccount('Sara', 100)` as an actual cookie made from it.
- Unlike plain dictionaries, a class locks in exact field names and attaches safe actions.

### 3. Tiny Example (Line-by-Line) — Creating Two Independent Objects from One Class
```python
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hp = 100

p1 = Player('Knight')
p2 = Player('Mage')
p1.hp = 80
print(p1.name, p1.hp, '|', p2.name, p2.hp)
```

1. `p1 = Player('Knight')` creates the first object (`p1.hp = 100`).
2. `p2 = Player('Mage')` creates a separate second object (`p2.hp` stays `100`!).
3. Changing `p1.hp = 80` leaves `p2.hp` untouched.

### Key Vocabulary
- **Class:** The blueprint (`Player`).
- **Object / Instance:** One item built from that blueprint (`p1`, `p2`).
- **Attribute:** A variable stored on an object (`p1.hp`).


### 4. Practical Example — Modeling a Book Object

```python
class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

b1 = Book('Python Basics', 180)
print(f'{b1.title} has {b1.pages} pages')
```

### Common Mistakes to Avoid

- Thinking `class` runs immediately—just like `def`, `class` defines the blueprint until you call `Book(...)`.

**Key Takeaway:** A class is a blueprint for creating independent objects that each hold their own attributes.


---

## 4.2 Inside `__init__` & What `self` Actually Means

> **Before You Start:** `self` looks strange only because other languages hide it. In Python, it is completely transparent once you see how Python passes it.

### 1. Definition
- **`__init__`:** The setup function that runs automatically when you create an object.
- **`self`:** Literally means **'this specific object calling the method right now'**.

### 2. Exact Syntax — How `self` Connects Attributes and Methods
```python
class Counter:
    def __init__(self) -> None:
        self.value = 0          # saved on THIS object

    def increment(self) -> None:
        self.value += 1         # updates THIS object's value

c = Counter()
c.increment()                   # Python runs Counter.increment(c)
```

- When you call `c.increment()`, Python automatically passes `c` as `self`!
- Writing `self.value = 0` saves `value` on the object; writing `value = 0` (no `self.`) disappears when `__init__` ends.

### 3. Tiny Example (Line-by-Line) — Watching `self` Keep Two Trackers Separate
```python
class StepTracker:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.steps = 0

    def walk(self, n: int) -> None:
        self.steps += n

a = StepTracker('Sara')
b = StepTracker('Alex')
a.walk(500)
b.walk(1200)
print(a.owner, a.steps, '|', b.owner, b.steps)
```

1. `a.walk(500)` runs with `self = a` -> `a.steps` becomes `500`.
2. `b.walk(1200)` runs with `self = b` -> `b.steps` becomes `1200`.

### Protecting Object State With Validation
Putting updates inside methods like `deposit(amount)` lets you reject bad inputs (`if amount <= 0: raise ValueError(...)`) in one place.


### 4. Practical Example — BankAccount With Validation Methods

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

acc = BankAccount('Sara', 100.0)
acc.deposit(50.0)
print('Balance:', acc.balance)
```

### Common Mistakes to Avoid

- Forgetting `self` in `def walk(n):` -> `TypeError`.
- Forgetting `self.` when saving attributes in `__init__`.

**Key Takeaway:** `self` is just the object calling the method, and methods let you validate and update state cleanly.


---

## 4.3 `@dataclass`, `__len__`, `__call__`, Composition & Modules

> **Before You Start:** Double-underscore ('dunder') methods simply teach your custom class how to work with `print()`, `len()`, and `()`.

### 1. Definition
- **`@dataclass`:** Auto-writes `__init__`, readable `print()` (`__repr__`), and `==` for data classes.
- **Composition:** Putting one object inside another (`Playlist` holding `Song` objects).

### 2. Exact Syntax — @dataclass, __len__ & __call__
```python
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    seconds: int

class TextCleaner:
    def __call__(self, text: str) -> str:
        return ' '.join(text.split()).lower()
```

- `@dataclass` eliminates `__init__` boilerplate for data objects.
- `__len__(self)` enables `len(playlist)`.
- `__call__(self, x)` lets a configured object be invoked like `cleaner('  Hi  ')`.

### 3. Tiny Example (Line-by-Line) — Playlist Composing Song Objects
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

pl = Playlist()
pl.add(Song('Intro', 90))
pl.add(Song('Main', 210))
print('Total:', pl.total_seconds())
```

1. `Song` holds data for one track cleanly.
2. `Playlist` holds a list of `Song` objects and sums `s.seconds` -> `300`.

### Splitting Files & Writing `pytest` Tests
Put `@dataclass` models in `models.py`, OOP logic in `analyzer.py` (no file I/O inside!), file reading in `cli.py`, and `def test_...(): assert ...` in `test_analyzer.py`.


### 4. Practical Example — Unit Testing an OOP Class

```python
def test_playlist_total() -> None:
    pl = Playlist()
    pl.add(Song('A', 60))
    assert pl.total_seconds() == 60
```

### Common Mistakes to Avoid

- Putting file reading inside OOP logic classes, making unit tests hard.

**Key Takeaway:** Use `@dataclass` for data, composition for cooperating objects, and keep I/O out of core classes so `pytest` is effortless.


---

## Hands-On Project: Modular OOP Log Analyzer Package

Refactor `legacy_monolith.py` into clean `models.py`, `analyzer.py`, `cli.py`, and `pytest` tests.

1. Inspect `legacy_monolith.py` to separate file reading from counting.
2. Create `LogEntry` and `LogReport` dataclasses in `models.py`.
3. Build `LogAnalyzer` in `analyzer.py` and pass `pytest`.
