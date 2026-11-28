"""Reference solutions with explanations."""


# --- 1.1: Warm-Up: Loop + Decision + Dictionary Summary ---
def grade_summary(scores: list[int]) -> dict[str, int]:
    counts = {'passed': 0, 'failed': 0}
    for s in scores:
        if s >= 60:
            counts['passed'] += 1
        else:
            counts['failed'] += 1
    return counts

if __name__ == '__main__':
    print(grade_summary([40, 60, 85, 59]))


# --- 1.2: One-Line Loop (Comprehension): Clean & Filter Names ---
def clean_names(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names if name.strip()]

if __name__ == '__main__':
    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))


# --- 1.3: Safe Functions: Fix the Shared Default List Bug ---
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    result = [] if tags is None else list(tags)
    if tag not in result:
        result.append(tag)
    return result

if __name__ == '__main__':
    print(add_tag('python'))
