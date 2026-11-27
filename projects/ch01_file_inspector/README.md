# Project (Chapter 1): Dataset Inspector & File Converter CLI

Read a CSV file safely with `Path` and `csv.DictReader`, count categories with `Counter`, and save a clean JSONL file.

## Architecture Steps

1. Check file existence with `pathlib.Path`.
2. Load CSV rows safely via `csv.DictReader` and `encoding='utf-8'`.
3. Count categories with `Counter` and export clean JSONL lines.

## Milestones

- [ ] Read CSV safely with Path and encoding='utf-8'
- [ ] Count categories with Counter & skip blank rows
- [ ] Write JSONL output and pass pytest
