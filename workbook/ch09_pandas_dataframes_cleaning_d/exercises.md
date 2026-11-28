# Workbook — Chapter 9: Pandas — DataFrames, Cleaning & Data Pipelines


---

## 9.1 Pandas Text Cleaning & Deduplication (`Foundation` · Pandas)

Write `clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame` sorted by `'id'`.

### Thinking Blueprint

- Drop nulls + `.copy()`, normalize spaces, sort by `'score'` desc before `drop_duplicates`.

### Progressive Hints

1. Reset index cleanly with `.reset_index(drop=True)`.

### Dry-Run Trace
Duplicate normalized texts retain the higher `'score'` row.

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

**High-Level Blocks:** Null filter, normalized dedup key, score-prioritized deduplication.


---

## 9.2 GroupBy Quality Metrics per Dataset Source (`Intermediate` · Pandas)

Write `summarize_sources(df: pd.DataFrame) -> pd.DataFrame` returning `['source', 'total_rows', 'valid_rows', 'avg_tokens']`.

### Thinking Blueprint

- Use `.groupby('source', as_index=False).agg(...)`.

### Progressive Hints

1. Cast `valid_rows` to `int`.

### Dry-Run Trace
`wiki` `[100, 200]` -> `total_rows=2, avg_tokens=150.0`.

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

**High-Level Blocks:** Named aggregations produce clean flat columns directly.
