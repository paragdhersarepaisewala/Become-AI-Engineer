# Project (Chapter 2): Dataset Inspector & File Converter CLI

Read a CSV file safely using `Path` and `csv.DictReader`, count labels with `Counter`, and export clean JSONL lines.

## Architecture Steps

1. Check file existence with `Path`.
2. Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.
3. Count categories with `Counter` and write clean JSONL output.

## Milestones

- [ ] Read CSV safely with Path & encoding='utf-8'
- [ ] Count categories using Counter & skip empty rows
- [ ] Write JSONL output and pass pytest
