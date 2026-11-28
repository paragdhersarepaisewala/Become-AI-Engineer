"""Reference solutions with explanations."""


# --- 10.1: Pydantic `BaseModel` & `@field_validator` ---
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


# --- 10.2: Pydantic Batch Filter Over Messy JSON Records ---
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
