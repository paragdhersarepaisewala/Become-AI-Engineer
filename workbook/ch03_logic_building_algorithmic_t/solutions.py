"""Reference solutions with explanations."""


# --- 3.1: State Machine Logic: Run-Length Encoder ---
def compress_runs(text: str) -> str:
    if not text:
        return ''
    parts: list[str] = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(f'{current}{count}')
            current = ch
            count = 1
    parts.append(f'{current}{count}')
    return ''.join(parts)


# --- 3.2: Hash Map Logic: First Unique Character Index ---
def first_unique_index(s: str) -> int:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


# --- 3.3: Dynamic Sliding Window: Longest Unique Substring ---
def longest_unique_len(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


# --- 3.4: Recursion & Call Stack: Flatten Nested Lists ---
def flatten(nested: list) -> list[int]:
    out: list[int] = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out
