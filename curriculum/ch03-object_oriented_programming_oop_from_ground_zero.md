# Chapter 3: Object-Oriented Programming (OOP) From Ground Zero

*Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, objects working together (composition), and splitting files.*

**Why It Matters:** If you skip OOP fundamentals, PyTorch (`nn.Module`), custom Datasets, and LangChain feel like magic. Once built slowly from first principles, classes feel completely natural.

**Skills Covered:** Why Classes?, __init__ & self, Methods & Validation, __repr__ & @dataclass, Composition, Modules & pytest


---

## 3.1 Why Do Classes Exist? (Solving the Loose-Variables Mess)

> **Before You Start:** Forget fancy textbook words like 'polymorphism' for now. Let's start with the real problem a `class` solves.

### 1. Definition
A **class** is a custom blueprint (like a form template) that bundles an item's **data** and the **functions that use that data** together into one neat **object**.

### 2. Exact Syntax — Before OOP (Messy) vs With a Class (Clean)
```python
# WITHOUT OOP (messy as soon as you have 5 accounts!):
acc1_owner = 'Sara'
acc1_balance = 100
acc2_owner = 'Alex'
acc2_balance = 50

# WITH OOP (1 blueprint, create as many accounts as you want):
class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance
```

- Think of `class BankAccount:` as a cookie cutter, and `acc1 = BankAccount('Sara', 100)` as an actual cookie made from it.
- Even dictionaries (`{'owner': 'Sara', 'balacne': 100}`) let typos slip through silently—a class locks in exact attribute names and attaches safe actions!

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

1. `class Player:` defines the blueprint (`name` and starting `hp = 100`).
2. `p1 = Player('Knight')` creates the first object (`p1.name='Knight'`, `p1.hp=100`).
3. `p2 = Player('Mage')` creates a completely separate second object (`p2.hp` is still `100`!).
4. Changing `p1.hp = 80` leaves `p2.hp` untouched!

### Key Vocabulary (In Plain English)
- **Class:** The blueprint (`Player`).
- **Instance / Object:** One real item built from that blueprint (`p1`, `p2`).
- **Attribute:** A variable living inside an object (`p1.hp`).


### 4. Practical Example — Modeling a Book Object

```python
class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

b1 = Book('Python Basics', 180)
b2 = Book('AI Systems', 320)
print(f'{b1.title} has {b1.pages} pages')
```

### Common Mistakes to Avoid

- Thinking `class` runs immediately—just like `def`, `class` only defines the blueprint until you create an object like `Book(...)`.

**Key Takeaway:** A class is a blueprint for creating independent objects that each hold their own attributes.


---

## 3.2 Inside `__init__` & What `self` Actually Means

> **Before You Start:** `self` looks strange only because other languages hide it. In Python, it is completely transparent once you see how Python passes it.

### 1. Definition
- **`__init__`:** The setup function that runs automatically the instant you create an object (`Player('Knight')`).
- **`self`:** Simply means **'this specific object calling the method right now'**.

### 2. Exact Syntax — How `self` Connects Attributes and Methods
```python
class Counter:
    def __init__(self) -> None:
        self.value = 0          # attach `value` to THIS object

    def increment(self) -> None:
        self.value += 1         # update THIS object's `value`

c = Counter()
c.increment()                   # Python runs Counter.increment(c)!
```

- When you call `c.increment()`, Python secretly translates it to `Counter.increment(c)`—passing `c` as `self`!
- That's why **every normal method inside a class takes `self` as its first parameter**.
- Inside `__init__`, writing `self.value = 0` saves `0` on the object forever. Writing `value = 0` (without `self.`) creates a temporary variable that disappears as soon as `__init__` finishes!

### 3. Tiny Example (Line-by-Line) — Watching `self` Keep Two Counters Separate
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

1. `a.walk(500)` runs `walk` with `self = a` -> `a.steps` becomes `500`.
2. `b.walk(1200)` runs `walk` with `self = b` -> `b.steps` becomes `1200`.
3. Prints `Sara 500 | Alex 1200`.

### Protecting Object State With Validation
Because updates go through a method (like `deposit(amount)` or `walk(n)`), you can guard against bad data in **one place** (`if amount <= 0: raise ValueError(...)`) instead of scattering checks across 10 files.


### 4. Practical Example — Safe BankAccount Methods With Guard Checks

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
print('Withdraw 200 ok?', acc.withdraw(200.0), '| Balance:', acc.balance)
```

### Common Mistakes to Avoid

- Forgetting `self` in `def walk(n):` -> crashes with `TypeError: walk() takes 1 positional argument but 2 were given`.
- Forgetting `self.` when setting attributes inside `__init__` (`steps = 0` instead of `self.steps = 0`).

**Key Takeaway:** `self` is just the object calling the method, and methods let you validate and update an object's state safely.


---

## 3.3 Making Classes Clean: `__repr__`, `@dataclass`, `__len__` & `__call__`

> **Before You Start:** If you ever tried `print(my_object)` and saw `<Book object at 0x000001A2F>`, this fixes that!

### 1. Definition
**Dunder ('double-underscore') methods** teach your custom class how to work with standard Python built-ins like `print()`, `len()`, `in`, and `()`.

### 2. Exact Syntax — The 4 Most Useful Shortcuts & Dunders
```python
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    seconds: int

# @dataclass auto-creates __init__, readable print() (__repr__), and == !
```

- `__repr__(self) -> str`: controls what `print(obj)` displays.
- `@dataclass`: decorator that writes `__init__`, `__repr__`, and `==` automatically for data-holding classes!
- `__len__(self) -> int`: lets callers write `len(my_playlist)`.
- `__call__(self, x)`: lets an object holding settings in `self` be called like a function: `cleaner('  hi  ')`.

### 3. Tiny Example (Line-by-Line) — Using `@dataclass` vs Plain Class
```python
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    seconds: int

s1 = Song('Focus Beat', 180)
s2 = Song('Focus Beat', 180)
print(s1)          # Song(title='Focus Beat', seconds=180)
print(s1 == s2)    # True!
```

1. Without `@dataclass`, `print(s1)` prints an ugly memory address and `s1 == s2` is `False`!
2. With `@dataclass`, Python prints all fields cleanly and compares values with `==`.

### Why `__call__` Matters Later in AI
When you build neural layers in PyTorch (`layer(x)`) or text steps in LangChain (`chain(prompt)`), they store configuration/weights in `self` and run via `__call__`.


### 4. Practical Example — A Small Callable Normalizer (`__call__`)

```python
class TextCleaner:
    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase

    def __call__(self, text: str) -> str:
        cleaned = ' '.join(text.split())
        return cleaned.lower() if self.lowercase else cleaned

clean = TextCleaner(lowercase=True)
print(clean('  Hello   AI  '))  # 'hello ai'
```

### Common Mistakes to Avoid

- Expecting `==` to compare fields on a normal class without `@dataclass` or `__eq__` (Python compares memory addresses by default!).

**Key Takeaway:** Use `@dataclass` for clean data objects, `__len__` for collections, and `__call__` when an object acts like a configured function.


---

## 3.4 Objects Working Together (Composition) & Splitting Files

> **Before You Start:** Real apps aren't 1 class—they are 2 or 3 small classes cooperating, organized across clean `.py` files.

### 1. Definition
- **Composition ('has-a'):** Putting one object inside another object (for example, a `Playlist` *has* a list of `Song` objects).
- **Modular Files:** Putting data models in `models.py`, logic classes in `player.py`, and tests in `test_player.py`.

### 2. Exact Syntax — Composition + Importing Across Files
```python
class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[Song] = []  # Playlist HAS Song objects

    def add(self, song: Song) -> None:
        self.songs.append(song)

    def __len__(self) -> int:
        return len(self.songs)
```

- `Song` knows about one song (`title`, `seconds`). `Playlist` knows how to hold and summarize many `Song`s.
- When splitting files, `from models import Song` lets `playlist.py` reuse `Song` without cramming everything into 1 huge script!

### 3. Tiny Example (Line-by-Line) — Playlist Holding Song Objects
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
print('Total seconds:', pl.total_seconds())
```

1. Creates two `Song` objects and adds them to `pl`.
2. `sum(s.seconds for s in self.songs)` loops through every `Song` object inside `pl` and sums `.seconds` -> `300`.

### Verifying Classes Automatically With `pytest`
Put `def test_playlist_total():` in `test_playlist.py` using `assert pl.total_seconds() == 300`, then run `python -m pytest` to verify every method in milliseconds.


### 4. Practical Example — Testing Your Class With `assert` / `pytest`

```python
def test_playlist_counts() -> None:
    pl = Playlist()
    pl.add(Song('A', 60))
    pl.add(Song('B', 120))
    assert pl.total_seconds() == 180
```

### Common Mistakes to Avoid

- Giving one giant class 15 unrelated jobs (reading files, parsing text, and printing reports) instead of splitting small cooperating classes.

**Key Takeaway:** Build small single-job classes that hold each other (composition), split them into clean `.py` modules, and test with `pytest`.


---

## Hands-On Project: Modular OOP Log Analyzer Package

Refactor `legacy_monolith.py` into clean `models.py` (`@dataclass`), `analyzer.py` (`class LogAnalyzer`), `cli.py`, and `pytest` tests.

1. Inspect `legacy_monolith.py` and separate file reading from counting.
2. Create `LogEntry` and `LogReport` dataclasses in `models.py`.
3. Build `LogAnalyzer` in `analyzer.py` and test with `pytest`.
