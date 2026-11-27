"""Reference solutions with explanations."""


# --- 6.1: Vectorized Standardization (Broadcasting + `axis`) ---
import numpy as np

def standardize_columns(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    mean = x.mean(axis=0, keepdims=True)
    std = x.std(axis=0, keepdims=True)
    safe_std = np.where(std == 0, 1.0, std)
    return (x - mean) / safe_std


# --- 6.2: Numerically Stable Softmax ---
import numpy as np

def stable_softmax(logits: np.ndarray) -> np.ndarray:
    logits = np.asarray(logits, dtype=float)
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)


# --- 6.3: Cosine Top-K Vector Retrieval ---
import numpy as np

def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:
    if k <= 0 or len(docs) == 0:
        return []
    docs = np.asarray(docs, dtype=float)
    query = np.asarray(query, dtype=float)
    doc_norms = np.maximum(np.linalg.norm(docs, axis=1, keepdims=True), 1e-12)
    q_norm = max(float(np.linalg.norm(query)), 1e-12)
    sims = (docs / doc_norms) @ (query / q_norm)
    return np.argsort(sims)[::-1][:k].tolist()
