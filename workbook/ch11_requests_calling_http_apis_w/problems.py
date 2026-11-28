"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 11.1: Safe HTTP Fetcher With `requests` & Timeout ---
import requests

def fetch_json_safe(url: str, timeout: float = 3.0):
    # TODO: GET url with timeout, raise_for_status, return json or None on RequestException
    pass


# --- 11.2: Automation: Fetch API + Validate With Pydantic + Save JSON ---
from pathlib import Path
import requests
from pydantic import BaseModel, Field, ValidationError

class ApiNote(BaseModel):
    id: int
    text: str = Field(min_length=1)

def sync_api_note(url: str, out_path: Path) -> bool:
    # TODO: fetch -> validate -> save JSON
    pass
