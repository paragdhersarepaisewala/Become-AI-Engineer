"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 10.1: Pydantic `BaseModel` & `@field_validator` ---
from pydantic import BaseModel, Field, field_validator

class Article(BaseModel):
    # TODO: define title, views, tags and strip/validate title
    pass

if __name__ == '__main__':
    print(Article(title='  Learn Pydantic ', views='12'))


# --- 10.2: Pydantic Batch Filter Over Messy JSON Records ---
from pydantic import BaseModel, Field, ValidationError

class PromptItem(BaseModel):
    prompt: str = Field(min_length=3)
    score: int = Field(ge=1, le=5)

def filter_valid_prompts(rows: list[dict]) -> list[PromptItem]:
    # TODO: validate each row and keep valid PromptItem objects
    pass
