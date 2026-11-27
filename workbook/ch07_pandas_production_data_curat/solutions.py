"""Reference solutions with explanations."""


# --- 7.1: Pandas Text Cleaning & Hash Deduplication ---
import pandas as pd

def clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame:
    out = df.dropna(subset=['text']).copy()
    out['clean_text'] = out['text'].astype(str).str.split().str.join(' ')
    out = out[out['clean_text'].str.len() >= min_len].copy()
    out['_norm'] = out['clean_text'].str.lower()
    out = out.sort_values('score', ascending=False).drop_duplicates(subset=['_norm'], keep='first')
    return out.drop(columns=['_norm']).sort_values('id').reset_index(drop=True)


# --- 7.2: GroupBy Quality Metrics per Dataset Source ---
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
