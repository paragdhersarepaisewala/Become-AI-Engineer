"""Reference solutions with explanations."""


# --- 4.1: Basic Logic: Find Largest Number Manually (No `max()`) ---
def find_max(nums: list[int]) -> int | None:
    if not nums:
        return None
    best = nums[0]
    for n in nums[1:]:
        if n > best:
            best = n
    return best

if __name__ == '__main__':
    print(find_max([-10, -3, -20]))


# --- 4.2: Grouping Logic: Group Words by First Letter ---
def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for raw in words:
        w = raw.strip()
        if not w:
            continue
        key = w[0].lower()
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return groups


# --- 4.3: State Machine Logic: Run-Length Encoder ---
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


# --- 4.4: Sliding Window: Longest Unique Substring ---
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
