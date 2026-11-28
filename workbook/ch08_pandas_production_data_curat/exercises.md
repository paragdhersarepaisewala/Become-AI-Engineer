# Workbook — Chapter 8: Pandas & Production Data Curation


---

## 8.1 Pandas Text Cleaning & Hash Deduplication (`Foundation` · Pandas)

Write `clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame`: drop null `'text'`, collapse whitespace into `'clean_text'`, keep `len >= min_len`, deduplicate case-insensitively keeping highest `'score'`, and sort by `'id'`.

### Thinking Blueprint

- Drop nulls + `.copy()`.
- Vectorized `.str.split().str.join(' ')` normalizes whitespace.
- Sort by `'score'` descending before `drop_duplicates`, then sort by `'id'`.

### Progressive Hints

1. Remember `.reset_index(drop=True)` after sorting.

### Dry-Run Trace
`'  Hello   AI world  '` (score 0.5) & `'hello ai world'` (score 0.95) -> keeps row with score 0.95.

### Answer & Explanation
```python
import pandas as pd

def clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame:
    out = df.dropna(subset=['text']).copy()
    out['clean_text'] = out['text'].astype(str).str.split().str.join(' ')
    out = out[out['clean_text'].str.len() >= min_len].copy()
    out['_norm'] = out['clean_text'].str.lower()
    out = out.sort_values('score', ascending=False).drop_duplicates(subset=['_norm'], keep='first')
    return out.drop(columns=['_norm']).sort_values('id').reset_index(drop=True)
```

**High-Level Blocks:** (1) Null & length filtering; (2) Normalized dedup key; (3) Score-prioritized deduplication.


---

## 8.2 GroupBy Quality Metrics per Dataset Source (`Intermediate` · Pandas)

Write `summarize_sources(df: pd.DataFrame) -> pd.DataFrame` returning `['source', 'total_rows', 'valid_rows', 'avg_tokens']` sorted by `'source'`.

### Thinking Blueprint

- Use `.groupby('source', as_index=False).agg(...)` with named aggregations.

### Progressive Hints

1. Cast `valid_rows` to `int`.

### Dry-Run Trace
Source `'wiki'` `[100, 200]`, `[True, False]` -> `total_rows=2, valid_rows=1, avg_tokens=150.0`.

### Answer & Explanation
```python
import pandas as pd

def summarize_sources(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby('source', as_index=False)
        .agg(total_rows=('tokens', 'count'), valid_rows=('is_valid', 'sum'), avg_tokens=('tokens', 'mean'))
        .sort_values('source')
        .reset_index(drop=True)
    )
    summary['valid_rows'] = summary['valid_rows'].astype(int)
    return summary
```

**High-Level Blocks:** Named aggregation produces flat column names directly without MultiIndex cleanup.
