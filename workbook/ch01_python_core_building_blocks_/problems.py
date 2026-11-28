"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 1.1: Warm-Up: Loop + Decision + Dictionary Summary ---
def grade_summary(scores: list[int]) -> dict[str, int]:
    # TODO: count how many scores are >= 60 vs < 60
    pass

if __name__ == '__main__':
    print(grade_summary([40, 60, 85, 59]))


# --- 1.2: One-Line Loop (Comprehension): Clean & Filter Names ---
def clean_names(names: list[str]) -> list[str]:
    # TODO: strip & lowercase non-empty names
    pass

if __name__ == '__main__':
    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))


# --- 1.3: Function Basics: Discount Price Calculator ---
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    # TODO: validate inputs, subtract discount%, and return rounded price
    pass

if __name__ == '__main__':
    print(apply_discount(100))
