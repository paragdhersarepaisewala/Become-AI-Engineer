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

**Key Takeaway:** Drop nulls, `.copy()`, and clean columns with `.str` before running aggregations.


---

## 9.2 `groupby().agg(...)` Named Aggregations, Sorting & Deduplication

> **Before You Start:** Plain `.groupby('src')['tokens'].mean()` only computes one metric. Real pipelines need counts, sums, and averages together with clean column names.

### 1. Definition
- **Named Aggregation (`.agg(new_col=('old_col', 'func'))`):** Computes multiple summary stats per group in one call with flat column names.
- **`.sort_values(..., ascending=False)` + `.drop_duplicates(..., keep='first')`:** Keeps the highest-scoring row when duplicates exist.

### 2. Exact Syntax — Named GroupBy Aggregation & Score-First Deduplication
```python
summary = (
    df.groupby('source', as_index=False)
    .agg(
        total_rows=('tokens', 'count'),
        valid_rows=('is_valid', 'sum'),
        avg_tokens=('tokens', 'mean'),
    )
    .sort_values('source')
    .reset_index(drop=True)
)
summary['valid_rows'] = summary['valid_rows'].astype(int)
```

- `new_name=('source_col', 'agg_func')`: supports `'count'`, `'sum'`, `'mean'`, `'min'`, `'max'`.
- `.astype(int)` converts True/False sum floats cleanly to integers.
- `.reset_index(drop=True)` resets messy row numbers `0, 2, 5` back to `0, 1, 2` after filtering or sorting.

### 3. Tiny Example (Line-by-Line) — Summarizing Dataset Sources
```python
import pandas as pd
df = pd.DataFrame([
    {'source': 'wiki', 'tokens': 100, 'is_valid': True},
    {'source': 'wiki', 'tokens': 200, 'is_valid': False},
    {'source': 'arxiv', 'tokens': 300, 'is_valid': True},
])
res = df.groupby('source', as_index=False).agg(
    total_rows=('tokens', 'count'),
    valid_rows=('is_valid', 'sum'),
    avg_tokens=('tokens', 'mean'),
)
print(res)
```

1. Groups rows by `'source'` (`arxiv` and `wiki`).
2. Computes all 3 summary columns cleanly in one table.

### Collapsing Whitespace in Pandas Columns
`df['text'].astype(str).str.split().str.join(' ')` collapses `'  Hello   AI  '` into `'Hello AI'` across every row without a Python loop!


### 4. Practical Example — Cleaning, Deduplicating & Keeping Max Score

```python
import pandas as pd

df = pd.DataFrame([
    {'id': 1, 'text': '  Hello   AI ', 'score': 0.5},
    {'id': 2, 'text': 'hello ai', 'score': 0.95},
])
out = df.copy()
out['clean'] = out['text'].str.split().str.join(' ').str.lower()
out = out.sort_values('score', ascending=False).drop_duplicates('clean', keep='first')
print(out.reset_index(drop=True))
```

### Common Mistakes to Avoid

- Forgetting `.reset_index(drop=True)` after sorting/deduplicating (leaves old index labels like `1` instead of `0`).

**Key Takeaway:** Use `.groupby(..., as_index=False).agg(...)` for flat multi-metric tables and sort before `.drop_duplicates(keep='first')`.


---

## Hands-On Project: End-to-End LLM Corpus Curation Pipeline

Clean messy JSONL/CSV text data, deduplicate via SHA-256, and export clean splits with source quality metrics.

1. Load raw records into Pandas and remove null/short noise.
2. Deduplicate by normalized text hash.
3. Produce `groupby` quality stats and save clean outputs.
