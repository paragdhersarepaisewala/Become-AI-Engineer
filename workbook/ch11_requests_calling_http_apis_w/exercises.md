# Workbook — Chapter 11: Requests — Calling HTTP APIs & Web Automations


---

## 11.1 Safe HTTP Fetcher With `requests` & Timeout (`Foundation` · Requests)

Write `fetch_json_safe(url: str, timeout: float = 3.0) -> dict | None` using `requests.get(url, timeout=timeout)`, calling `resp.raise_for_status()`, returning `resp.json()`, or returning `None` on `requests.RequestException`.

### Thinking Blueprint

- Wrap `requests.get`, `raise_for_status()`, and `.json()` inside `try / except requests.RequestException:`.

### Progressive Hints

1. Always pass `timeout=timeout`.

### Dry-Run Trace
HTTP 200 -> parsed dict; HTTP 404 or connection failure -> `None`.

### Answer & Explanation
```python
import requests

def fetch_json_safe(url: str, timeout: float = 3.0):
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return None
```

**High-Level Blocks:** `timeout` avoids infinite hangs, `raise_for_status()` catches 4xx/5xx errors, and `RequestException` handles both HTTP and connection errors.


---

## 11.2 Automation: Fetch API + Validate With Pydantic + Save JSON (`Intermediate` · Requests)

Given `ApiNote(BaseModel)` (`id: int`, `text: str` min_length=1), write `sync_api_note(url: str, out_path: Path) -> bool` that fetches JSON via `requests.get(url, timeout=3.0)`, validates it as `ApiNote`, saves `.model_dump_json()` to `out_path` (creating parents), and returns `True` (or `False` on network/validation failure).

### Thinking Blueprint

- Fetch -> validate with `ApiNote.model_validate(...)` -> `out_path.parent.mkdir(...)` -> `write_text`.

### Progressive Hints

1. Catch `(requests.RequestException, ValidationError)`.

### Dry-Run Trace
Valid API reply -> saved to `out_path` -> `True`; bad JSON -> `False`.

### Answer & Explanation
```python
from pathlib import Path
import requests
from pydantic import BaseModel, Field, ValidationError

class ApiNote(BaseModel):
    id: int
    text: str = Field(min_length=1)

def sync_api_note(url: str, out_path: Path) -> bool:
    try:
        resp = requests.get(url, timeout=3.0)
        resp.raise_for_status()
        note = ApiNote.model_validate(resp.json())
    except (requests.RequestException, ValidationError, ValueError):
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(note.model_dump_json(indent=2), encoding='utf-8')
    return True
```

**High-Level Blocks:** Fetch -> Validate -> Save is the core pattern of every reliable API ingestion automation.
