"""Reference solutions with explanations."""


# --- 11.1: Safe HTTP Fetcher With `requests` & Timeout ---
import requests

def fetch_json_safe(url: str, timeout: float = 3.0):
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return None


# --- 11.2: Automation: Fetch API + Validate With Pydantic + Save JSON ---
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
