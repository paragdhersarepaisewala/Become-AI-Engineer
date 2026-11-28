# Chapter 10: Pydantic — Data Validation, Models & Serialization

*BaseModel, automatic type checking, Field constraints, @field_validator, nested models, ValidationError, and JSON serialization.*

**Why It Matters:** Before you call external APIs with `requests` or build servers with `FastAPI` or tools with `FastMCP`, you need **Pydantic**—the #1 library in Python AI engineering for validating messy JSON, enforcing schemas, and preventing silent data bugs.

**Skills Covered:** Pydantic, BaseModel, Field, @field_validator, Nested Models, ValidationError


---

## 10.1 `BaseModel` & Automatic Validation (Why Dicts Aren't Enough)

> **Before You Start:** Remember `@dataclass` from Chapter 4? `@dataclass` does NOT check if someone passes `'twenty'` for `age: int`. **Pydantic `BaseModel` DOES check and enforces rules automatically!**

### 1. Definition
**Pydantic** lets you define Python classes inheriting from `BaseModel` that automatically convert valid inputs (like `'25'` -> `25`), reject invalid inputs with a clear `ValidationError`, and convert cleanly to/from JSON.

### 2. Exact Syntax — Defining a `BaseModel` & Catching `ValidationError`
```python
from pydantic import BaseModel, Field, ValidationError

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=13)       # ge = greater than or equal to 13
    is_active: bool = True        # default value
    tags: list[str] = Field(default_factory=list)  # fresh [] per instance!

user = UserProfile(username='sara', age='22')  # converts '22' -> 22!
print(user.model_dump())          # converts back to plain dict
```

- `BaseModel`: parent class giving your model validation + JSON superpowers.
- `Field(min_length=3, ge=13)`: adds strict rules (`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`).
- `user.model_dump()` -> Python `dict`; `user.model_dump_json()` -> JSON string; `UserProfile.model_validate_json(raw_str)` -> parses & validates JSON in 1 call!

### 3. Tiny Example (Line-by-Line) — Watching Pydantic Reject Bad Data Automatically
```python
from pydantic import BaseModel, Field, ValidationError

class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)

print(Item(name='Book', price='19.5'))
try:
    Item(name='Book', price=-5)
except ValidationError as err:
    print('Rejected!', err.errors()[0]['msg'])
```

1. `Item(name='Book', price='19.5')` succeeds and converts `'19.5'` to float `19.5`.
2. `Item(name='Book', price=-5)` fails `gt=0` and raises `ValidationError` cleanly!

### Why Pydantic Comes *Before* `requests`, `FastAPI` & `FastMCP`
- With **`requests`**, external APIs return messy JSON—Pydantic validates it immediately.
- With **`FastAPI`**, your endpoints use Pydantic models to reject invalid user JSON automatically.
- With **`FastMCP`**, AI agent tool inputs and outputs are typed with Pydantic schemas!


### 4. Practical Example — Validating a JSON File of Records Safely

```python
from pydantic import BaseModel, Field, ValidationError

class PromptSample(BaseModel):
    prompt: str = Field(min_length=3)
    rating: int = Field(ge=1, le=5)

raw_rows = [
    {'prompt': 'Explain loops', 'rating': 5},
    {'prompt': 'Hi', 'rating': 5},        # too short!
    {'prompt': 'Explain OOP', 'rating': 9}, # rating > 5!
]

valid = []
for row in raw_rows:
    try:
        valid.append(PromptSample.model_validate(row))
    except ValidationError:
        continue
print('Valid samples:', valid)
```

### Common Mistakes to Avoid

- Trying to modify a Pydantic model like a dict (`user['age']` instead of `user.age`).
- Using old Pydantic v1 `.dict()` / `.parse_raw()` instead of v2 `.model_dump()` / `.model_validate_json()`.

**Key Takeaway:** Use Pydantic `BaseModel` + `Field` to turn untrusted dicts/JSON into guaranteed, typed Python objects.


---

## 10.2 Custom `@field_validator` & Nested Models

> **Before You Start:** Built-in `Field` rules handle lengths and numbers—but what if you want to strip whitespace or reject blank `'   '` strings?

### 1. Definition
- **`@field_validator`:** A custom Python check you attach to any field (for cleaning strings or checking custom business rules).
- **Nested Models:** Putting one `BaseModel` inside another (e.g., an `Order` containing a list of `OrderItem` models).

### 2. Exact Syntax — Custom Field Validator + Nested Model
```python
from pydantic import BaseModel, field_validator

class Tag(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def clean_name(cls, v: str) -> str:
        cleaned = v.strip().lower()
        if not cleaned:
            raise ValueError('name cannot be blank')
        return cleaned
```

- `@field_validator('name')` runs automatically whenever `Tag(name=...)` is created.
- `@classmethod` is required by Pydantic v2 (`cls` is the `Tag` class, `v` is the incoming value).
- Return the cleaned value (like `cleaned`), or `raise ValueError(...)` to fail validation.

### 3. Tiny Example (Line-by-Line) — Nested Model Validating a Full Config
```python
from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    name: str
    temperature: float = Field(ge=0.0, le=2.0)

class AppSettings(BaseModel):
    app_name: str
    llm: ModelConfig

cfg = AppSettings(app_name='Tutor', llm={'name': 'qwen', 'temperature': 0.3})
print(cfg.llm.name, cfg.llm.temperature)
```

1. `AppSettings` accepts a nested dict for `llm` and automatically validates it into a `ModelConfig` object!
2. `cfg.llm.name` accesses nested fields with dot-notation and full type safety.

### Saving Validated Models Directly to JSON Files
`Path('config.json').write_text(cfg.model_dump_json(indent=2), encoding='utf-8')` saves nicely formatted JSON in 1 line, and `AppSettings.model_validate_json(...)` loads & re-validates it!


### 4. Practical Example — Round-Trip Config Validation + File Save

```python
from pathlib import Path
import tempfile
from pydantic import BaseModel, Field, field_validator

class Note(BaseModel):
    title: str = Field(min_length=1)
    tags: list[str] = []

    @field_validator('title')
    @classmethod
    def strip_title(cls, v: str) -> str:
        s = v.strip()
        if not s:
            raise ValueError('Title cannot be blank')
        return s

with tempfile.TemporaryDirectory() as d:
    p = Path(d) / 'note.json'
    n = Note(title='  Learn Pydantic  ', tags=['ai'])
    p.write_text(n.model_dump_json(indent=2), encoding='utf-8')
    loaded = Note.model_validate_json(p.read_text(encoding='utf-8'))
    print(loaded)
```

### Common Mistakes to Avoid

- Forgetting `@classmethod` below `@field_validator(...)`.
- Using mutable `tags: list[str] = []` in normal Python `def` vs Pydantic (in Pydantic `BaseModel`, `tags: list[str] = []` IS actually copied per instance safely, though `Field(default_factory=list)` is even cleaner!).

**Key Takeaway:** Use `@field_validator` to normalize/reject custom values, and nest `BaseModel` classes for complex configs & API payloads.


---

## Hands-On Project: Typed Dataset & Config Validator (`Pydantic`)

Build nested Pydantic models with `@field_validator` to validate raw JSONL files, log bad rows, and save clean validated JSON.

1. Define nested Pydantic schemas with `Field` and `@field_validator`.
2. Read raw JSONL records and separate valid objects from `ValidationError` rows.
3. Write clean validated JSON output and verify with `pytest`.
