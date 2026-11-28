# Chapter 9: Pandas — DataFrames, Cleaning & Data Pipelines

*Series & DataFrames, reading/writing CSV & JSON, loc vs iloc, filtering, .str cleaning, groupby, and deduplication.*

**Why It Matters:** Training ML models or fine-tuning LLMs on duplicate, null, or noisy text wastes compute and causes train/test leakage.

**Skills Covered:** Pandas, DataFrame, loc vs iloc, read_csv / to_json, GroupBy, Deduplication


---

## 9.1 DataFrames, `loc`/`iloc`, File I/O & Cleaning Datasets

> **Before You Start:** Think of a Pandas `DataFrame` as an in-memory Excel table where each column is a fast Series.

### 1. Definition
A **DataFrame** holds rows and named columns (`df['text']`, `df['score']`). Instead of looping row-by-row, you filter and transform entire columns at once using boolean masks and `.str` methods.

### 2. Exact Syntax — Essential DataFrame Syntax
```python
import pandas as pd

df = pd.DataFrame([{'text': ' Hi ', 'score': 0.9}, {'text': None, 'score': 0.2}])
clean = df.dropna(subset=['text']).copy()
clean['text'] = clean['text'].str.strip()
high = clean[clean['score'] >= 0.8]
df.loc[0, 'text']   # select by label
df.iloc[0, 0]       # select by integer position
```

- `.dropna(subset=['text'])`: removes rows where `'text'` is `None`/`NaN`.
- `.copy()` after filtering prevents Pandas `SettingWithCopyWarning` when editing columns later.
- `loc` uses **labels** (`df.loc[0:2]` includes `2`); `iloc` uses integer **positions** (`df.iloc[0:2]` stops before `2`).

### 3. Tiny Example (Line-by-Line) — Filtering & Summarizing by Source
```python
import pandas as pd
df = pd.DataFrame([
    {'src': 'wiki', 'tokens': 100},
    {'src': 'wiki', 'tokens': 200},
    {'src': 'docs', 'tokens': 300},
])
print(df.groupby('src', as_index=False)['tokens'].mean())
```

1. Builds a 3-row table with `'src'` and `'tokens'`.
2. `groupby('src', as_index=False)` groups `'wiki'` rows together and `'docs'` rows together.
3. `.mean()` computes average tokens per source.

### Reading & Exporting Cleaned Files
Use `pd.read_csv('raw.csv')` / `pd.read_json('raw.jsonl', lines=True)` to load datasets, and `clean.to_csv('clean.csv', index=False)` to save without extra index columns.


### 4. Practical Example — Hash Deduplication Pipeline

```python
import hashlib
import pandas as pd

def text_hash(s: str) -> str:
    return hashlib.sha256(' '.join(s.lower().split()).encode('utf-8')).hexdigest()

df = pd.DataFrame([
    {'id': 1, 'text': 'Hello   AI'},
    {'id': 2, 'text': 'hello ai'},
])
df['hash'] = df['text'].map(text_hash)
print(df.drop_duplicates(subset=['hash']).reset_index(drop=True))
```

### Common Mistakes to Avoid

- Using `.iterrows()` to edit rows instead of vectorized `.str` / `.map()`.
- Forgetting `.copy()` after filtering before adding new columns.

**Key Takeaway:** Drop nulls, `.copy()`, clean columns with `.str`, deduplicate with hashes, and summarize with `.groupby().agg()`.


---

## Hands-On Project: End-to-End LLM Corpus Curation Pipeline

Clean messy JSONL/CSV text data, deduplicate via SHA-256, and export clean splits with source quality metrics.

1. Load raw records into Pandas and remove null/short noise.
2. Deduplicate by normalized text hash.
3. Produce `groupby` quality stats and save clean outputs.
