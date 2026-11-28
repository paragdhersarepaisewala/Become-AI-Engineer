"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 7.1: Vectorized Standardization (Broadcasting + `axis`) ---
import numpy as np

def standardize_columns(x: np.ndarray) -> np.ndarray:
    # TODO: normalize columns safely
    pass


# --- 7.2: Numerically Stable Softmax ---
import numpy as np

def stable_softmax(logits: np.ndarray) -> np.ndarray:
    # TODO: stable softmax along axis=-1
    pass


# --- 7.3: Cosine Top-K Vector Retrieval ---
import numpy as np

def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:
    # TODO: return indices of top-k cosine-similar rows
    pass
