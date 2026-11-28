"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 9.1: Pydantic Contract & FastAPI `/tokenize` Endpoint ---
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# TODO: define TokenizeRequest and POST /tokenize


# --- 9.2: Microservice Pattern: Async Job Queue & Worker ---
import asyncio

class JobBroker:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()
        self.jobs: dict[str, dict] = {}
        self._counter = 0

    def submit(self, payload: str) -> str:
        pass

    async def process_one(self) -> bool:
        pass
