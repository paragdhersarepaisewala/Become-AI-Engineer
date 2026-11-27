# Chapter 2: Object-Oriented Programming (OOP) & Breaking the Monolith

*Classes, self, __init__, dataclasses, composition vs inheritance, dunder methods (__call__, __len__), and modular files.*

**Why It Matters:** Loose scripts with global variables turn messy fast. Plus, PyTorch (`nn.Module`), custom Datasets (`__len__`, `__getitem__`), and LangChain Runnables are all built using OOP classes.

**Skills Covered:** class & self, __init__, @dataclass, Composition, Dunder Methods, Modularity


---

## 2.1 Classes, `__init__` & `self` (Bundling Data + Functions)

> **Before You Start:** If you have ever wondered what `self` means inside `def method(self):`, this explains it cleanly.

### 1. Definition
A **class** is a blueprint for creating objects that bundle **data (attributes)** and **actions (methods)** together in one place, instead of passing 5 separate variables into every function.

### 2. Exact Syntax — Defining a Class & Creating Instances
```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

acc = BankAccount('Sara', 100.0)  # calls __init__ automatically
acc.deposit(50.0)                 # acc becomes `self` inside deposit!
```

- `__init__` (constructor) runs once automatically when you create `BankAccount(...)`.
- `self` means **this specific object**. If you create `acc1` and `acc2`, `self` keeps their balances separate.
- `self.balance` is an **attribute** (data attached to the object). `deposit` is a **method** (a function inside a class).

### 3. Tiny Example (Line-by-Line) — Two Independent Counter Objects
```python
class CounterBox:
    def __init__(self) -> None:
        self.count = 0

    def add_one(self) -> None:
        self.count += 1

a = CounterBox()
b = CounterBox()
a.add_one()
print(a.count, b.count)
```

1. `a = CounterBox()` creates box `a` with `a.count = 0`.
2. `b = CounterBox()` creates a separate box `b` with `b.count = 0`.
3. `a.add_one()` runs with `self = a`, so `a.count` becomes `1` while `b.count` stays `0`!

### Shortcut for Pure Data Classes: `@dataclass`
When a class's only job is holding fields (like `Document(doc_id, text)`), writing `self.x = x` ten times gets tedious. Putting `@dataclass` above a class makes Python write `__init__`, nice `print()` output (`__repr__`), and `==` comparisons automatically!


### 4. Practical Example — @dataclass + Stateful DocumentStore

```python
from dataclasses import dataclass

# Block 1: Passive data record — @dataclass auto-writes __init__ and __repr__
@dataclass
class Document:
    doc_id: str
    text: str

# Block 2: Stateful service class owning its dictionary of documents
class DocumentStore:
    def __init__(self) -> None:
        self._docs: dict[str, Document] = {}

    def add(self, doc: Document) -> None:
        self._docs[doc.doc_id] = doc

    def get(self, doc_id: str) -> Document | None:
        return self._docs.get(doc_id)
```

### Common Mistakes to Avoid

- Forgetting `self` as the first parameter of a method (`def add(doc):` crashes with `TypeError` when called as `store.add(doc)`!).
- Forgetting `self.` when saving attributes inside `__init__` (`count = 0` creates a temporary local variable that vanishes after `__init__`!).

**Key Takeaway:** A class groups data (`self.x`) and actions (`def method(self)`). Use `@dataclass` for simple data records.


---

## 2.2 Dunder Methods (`__len__`, `__call__`) & Composition

> **Before You Start:** Double-underscore ('dunder') methods look weird at first, but they just connect your class to built-in Python syntax like `len(x)` and `x()`.

### 1. Definition
- **Dunder methods (`__name__`):** Special hooks Python calls behind the scenes (`len(obj)` calls `obj.__len__()`; `obj(x)` calls `obj.__call__(x)`).
- **Composition:** Building a bigger object by storing smaller helper objects inside `self` (plugging LEGO bricks together) instead of deep inheritance.

### 2. Exact Syntax — __len__, __contains__, __call__ & Composition
```python
class WordCleaner:
    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase

    def __call__(self, text: str) -> str:
        out = ' '.join(text.split())
        return out.lower() if self.lowercase else out

cleaner = WordCleaner(lowercase=True)
cleaner('  Hello   AI  ')  # invokes __call__ -> 'hello ai'
```

- `__len__(self)` -> lets callers run `len(my_object)`.
- `__contains__(self, item)` -> lets callers run `if 'id1' in my_store:`.
- `__call__(self, x)` -> lets an object holding config/weights in `self` be called like a function `model(x)`!

### 3. Tiny Example (Line-by-Line) — Making `len(bag)` Work on a Custom Class
```python
class Bag:
    def __init__(self) -> None:
        self.items = []
    def add(self, x) -> None:
        self.items.append(x)
    def __len__(self) -> int:
        return len(self.items)

b = Bag()
b.add('apple')
print(len(b))
```

1. `Bag` stores a private list `self.items`.
2. Defining `__len__` teaches Python what `len(b)` should return.
3. `print(len(b))` prints `1`.

### Why AI Frameworks Love Composition + `__call__`
Both **PyTorch (`nn.Module`)** and **LangChain (`Runnable`)** work by composing small objects (`step1`, `step2`) inside a pipeline and calling them like functions!


### 4. Practical Example — Composable Pipeline Using Small `__call__` Steps

```python
class StripStep:
    def __call__(self, text: str) -> str:
        return ' '.join(text.split())

class LowerStep:
    def __call__(self, text: str) -> str:
        return text.lower()

# Block 1: Composition — Pipeline HAS a list of steps (no inheritance needed)
class Pipeline:
    def __init__(self, steps: list) -> None:
        self.steps = steps

    def __call__(self, text: str) -> str:
        for step in self.steps:
            text = step(text)
        return text

pipe = Pipeline([StripStep(), LowerStep()])
print(pipe('  Hello   WORLD  '))  # 'hello world'
```

### Common Mistakes to Avoid

- Creating 4-level inheritance trees (`class SmartCleaner(BaseCleaner(Helper))`) when passing a helper object into `__init__` is cleaner and easier to test.

**Key Takeaway:** Use `__call__` to make configured objects act like functions, and compose small independent classes together.


---

## 2.3 Breaking Monoliths into Modular Files & `pytest`

> **Before You Start:** A 'monolith' is one giant `.py` file where file loading, logic, and `print()` are tangled together so you can't test anything cleanly.

### 1. Definition
**Modular architecture** splits your code by job: data definitions (`models.py`), pure logic/classes (`analyzer.py`), file/CLI wiring (`cli.py`), and automated checks (`test_*.py`).

### 2. Exact Syntax — Writing a `pytest` Unit Test
```python
def test_something() -> None:
    actual = my_function('input')
    assert actual == 'expected'
```

- Any file starting with `test_` and function starting with `test_` is discovered automatically when you run `python -m pytest`.
- `assert condition` passes silently if True, and prints a clear diff if False.

### 3. Tiny Example (Line-by-Line) — Separating Pure Logic from File I/O
```python
# Pure function: takes a list of strings, returns a dict (no open() inside!)
def count_errors(lines: list[str]) -> int:
    return sum(1 for line in lines if '[ERROR]' in line)

def test_count_errors() -> None:
    assert count_errors(['[INFO] ok', '[ERROR] fail']) == 1
```

1. `count_errors` does NOT open any file—it accepts `list[str]` directly.
2. Because it has zero file I/O, `test_count_errors` can test it in 1 millisecond with a tiny fake list!

When you separate **pure logic** from **file/terminal I/O**, bugs become trivial to isolate and every change is verified automatically by `pytest`.


### 4. Practical Example — 3-File Package Layout

```python
# models.py   -> @dataclass LogEntry, LogReport
# analyzer.py -> class LogAnalyzer (pure logic, zero open/print)
# cli.py      -> uses Path.open() to read file, calls LogAnalyzer, prints summary
# test_analyzer.py -> pytest functions passing fake lists directly to LogAnalyzer
```

### Common Mistakes to Avoid

- Hardcoding `open('server.log')` inside parsing functions, making unit tests impossible without creating real files.

**Key Takeaway:** Keep file/network I/O at the edges (`cli.py`) and pure OOP/logic in testable modules.


---

## Hands-On Project: Modular OOP Log Analyzer Package

Refactor `legacy_monolith.py` into `models.py`, `analyzer.py`, and `cli.py` with a passing `pytest` suite.

1. Inspect `legacy_monolith.py` to separate parsing from printing.
2. Create `LogEntry` and `LogReport` dataclasses in `models.py`.
3. Implement `LogAnalyzer` in `analyzer.py` and verify with `pytest`.
