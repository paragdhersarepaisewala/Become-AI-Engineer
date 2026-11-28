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


# --- 1.3: Function Basics: Discount Price Calculator ---
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError('Invalid input')
    saved = price * (discount_percent / 100)
    return round(price - saved, 2)

if __name__ == '__main__':
    print(apply_discount(100))
    print(apply_discount(80, 25))
