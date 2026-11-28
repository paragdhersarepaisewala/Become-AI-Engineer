# Project (Chapter 9): End-to-End LLM Corpus Curation Pipeline

Clean messy JSONL/CSV text data, deduplicate via SHA-256, and export clean splits with source quality metrics.

## Architecture Steps

1. Load raw records into Pandas and remove null/short noise.
2. Deduplicate by normalized text hash.
3. Produce `groupby` quality stats and save clean outputs.

## Milestones

- [ ] Ingest & normalize raw text records
- [ ] Implement normalized hash deduplication
- [ ] Generate quality summary & export clean CSV/JSONL
