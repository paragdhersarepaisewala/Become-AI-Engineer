# Workbook — Chapter 10: Pydantic — Data Validation, Models & Serialization


---

## 10.1 Pydantic `BaseModel` & `@field_validator` (`Foundation` · Pydantic)

Create `class Article(BaseModel)` with:
- `title: str` (stripped; raise `ValueError` if blank or length < 3 after stripping)
- `views: int = Field(default=0, ge=0)`
- `tags: list[str] = Field(default_factory=list)`

### Thinking Blueprint

- Use `@field_validator('title')` + `@classmethod` to strip whitespace and check `len(cleaned) < 3`.

### Progressive Hints

1. Check length *after* stripping inside the validator so `'  a '` is rejected cleanly.

### Dry-Run Trace
`Article(title='  Learn Pydantic ', views='12')` -> `title='Learn Pydantic'`, `views=12`.

### Answer & Explanation
```python
from pydantic import BaseModel, Field, field_validator

class Article(BaseModel):
    title: str
    views: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list)

    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        cleaned = v.strip()
        if len(cleaned) < 3:
            raise ValueError('title must have at least 3 characters')
        return cleaned

if __name__ == '__main__':
    print(Article(title='  Learn Pydantic ', views='12'))
```

**High-Level Blocks:** Pydantic auto-coerces `'12' -> 12` while `@field_validator` cleans and guards string rules.


---

## 10.2 Pydantic Batch Filter Over Messy JSON Records (`Intermediate` · Pydantic)

Define `PromptItem(BaseModel)` (`prompt: str` min_length=3, `score: int` `1..5`) and `filter_valid_prompts(rows: list[dict]) -> list[PromptItem]` returning only rows that pass validation.

### Thinking Blueprint

- Loop over `rows`, call `PromptItem.model_validate(row)` inside `try / except ValidationError:`.

### Progressive Hints

1. Import `ValidationError` from `pydantic`.

### Dry-Run Trace
Invalid rows raise `ValidationError` and are skipped cleanly.

### Answer & Explanation
```python
from pydantic import BaseModel, Field, ValidationError

class PromptItem(BaseModel):
    prompt: str = Field(min_length=3)
    score: int = Field(ge=1, le=5)

def filter_valid_prompts(rows: list[dict]) -> list[PromptItem]:
    valid: list[PromptItem] = []
    for row in rows:
        try:
            valid.append(PromptItem.model_validate(row))
        except ValidationError:
            continue
    return valid
```

**High-Level Blocks:** `model_validate` + `ValidationError` cleanly separates good training data from bad rows.
