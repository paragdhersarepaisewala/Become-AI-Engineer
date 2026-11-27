# Chapter 7: Pandas & Production Data Curation

*DataFrames, loc vs iloc, filtering, string cleaning, groupby summaries, and hash deduplication.*

**Why It Matters:** Training ML models or fine-tuning LLMs on duplicate, null, or noisy text wastes compute and causes train/test leakage.

**Skills Covered:** DataFrame, loc vs iloc, Boolean Masks, .str Cleaning, GroupBy, Deduplication


---

## 7.1 DataFrames, `loc`/`iloc` & Cleaning Datasets Without Loops

> **Before You Start:** Think of a Pandas `DataFrame` as an in-memory Excel table where each column is a fast NumPy-backed `Series`.

### 1. Definition
A **DataFrame** holds rows and named columns (`df['text']`, `df['score']`). Instead of looping row-by-row, you filter and transform entire columns at once using boolean masks and `.str` methods.

### 2. Exact Syntax — Essential DataFrame Syntax
```python
import pandas as pd

df = pd.DataFrame([{'text': ' Hi ', 'score': 0.9}, {'text': None, 'score': 0.2}])
clean = df.dropna(subset=['text']).copy()         # drop missing text
clean['text'] = clean['text'].str.strip()         # clean whole column
high = clean[clean['score'] >= 0.8]               # boolean filter
df.loc[0, 'text']     # select by label
df.iloc[0, 0]         # select by integer row/col position
```

- `.dropna(subset=['text'])`: removes rows where `'text'` is `None`/`NaN`.
- `.copy()` after filtering prevents Pandas `SettingWithCopyWarning` when you edit columns later.
- `loc` uses row/column **labels** (`df.loc[0:2]` includes `2`); `iloc` uses integer **positions** (`df.iloc[0:2]` stops before `2`).

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
3. `.mean()` computes average tokens per source: `docs -> 300.0`, `wiki -> 150.0`.

### Deduplicating Text Datasets Before Training
Sorting by quality score descending and calling `.drop_duplicates(subset=['_norm'], keep='first')` ensures only the best version of duplicate records stays in your training corpus.


### 4. Practical Example — Hash Deduplication Pipeline

```python
import hashlib
import pandas as pd

def text_hash(s: str) -> str:
    norm = ' '.join(s.lower().split())
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()

def curate(df: pd.DataFrame) -> pd.DataFrame:
    out = df.dropna(subset=['text']).copy()
    out['hash'] = out['text'].map(text_hash)
    return out.drop_duplicates(subset=['hash']).reset_index(drop=True)
```

### Common Mistakes to Avoid

- Using `.iterrows()` to modify rows (very slow!). Use `.str`, `.map()`, or vectorized math.
- Forgetting `.copy()` after slicing a DataFrame before adding new columns.

**Key Takeaway:** Drop nulls, `.copy()`, clean columns with `.str`, deduplicate with hashes, and summarize with `.groupby().agg()`.


---

## Hands-On Project: End-to-End LLM Corpus Curation Pipeline

Clean messy JSONL text data, deduplicate via SHA-256, and generate per-source quality metrics.

1. Load raw records into Pandas and remove null/short noise.
2. Deduplicate by normalized text hash.
3. Produce `groupby` quality stats and clean splits.
