# Project (Chapter 2): Dataset Inspector & File Converter CLI

Read a messy CSV file safely using `Path` and `csv.DictReader`, filter invalid rows, and export clean JSONL lines.

## Architecture Steps

1. Check file existence with `Path`.
2. Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.
3. Write clean JSONL lines and verify with `pytest`.

## Milestones

- [ ] Read CSV safely with Path & encoding='utf-8'
- [ ] Filter invalid rows cleanly
- [ ] Write JSONL output and pass pytest
