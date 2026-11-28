# Project (Chapter 8): End-to-End LLM Corpus Curation Pipeline

Clean messy JSONL text data, deduplicate via SHA-256, and generate per-source quality metrics.

## Architecture Steps

1. Load raw records into Pandas and remove null/short noise.
2. Deduplicate by normalized text hash.
3. Produce `groupby` quality stats and clean splits.

## Milestones

- [ ] Ingest & normalize raw text records
- [ ] Implement normalized hash deduplication
- [ ] Generate quality summary & splits
