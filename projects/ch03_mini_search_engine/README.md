# Project (Chapter 3): Pure-Python Text Tokenizer & Inverted Index Search Engine

Build a keyword search engine mapping each word to matching document IDs using hash maps.

## Architecture Steps

1. Write `tokenize(text)` normalizing lowercase words.
2. Build `InvertedIndex` class mapping `word -> set of doc_ids`.
3. Implement ranked `AND` / `OR` queries + `pytest`.

## Milestones

- [ ] Implement text normalization & tokenizer
- [ ] Build InvertedIndex class with O(1) lookup
- [ ] Implement ranked search queries + pytest
