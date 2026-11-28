# Project (Chapter 10): Typed Dataset & Config Validator (`Pydantic`)

Build nested Pydantic models with `@field_validator` to validate raw JSONL files, log bad rows, and save clean validated JSON.

## Architecture Steps

1. Define nested Pydantic schemas with `Field` and `@field_validator`.
2. Read raw JSONL records and separate valid objects from `ValidationError` rows.
3. Write clean validated JSON output and verify with `pytest`.

## Milestones

- [ ] Define Pydantic schemas with Field & @field_validator
- [ ] Validate file records catching ValidationError cleanly
- [ ] Save clean JSON & pass pytest
