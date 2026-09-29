"""Five exercises on conditionals, validation, and grading."""

import string


# --------------------------------------------------------------------------
# Task 1: age category
# --------------------------------------------------------------------------
def age_category(age: int) -> str:
    """Return the life-stage category for ``age``."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 12:
        return "child"
    if age <= 17:
        return "teenager"
    if age <= 65:
        return "adult"
    return "senior"


def ask_age() -> None:
    try:
        age = int(input("Enter your age: "))
        print(f"Category: {age_category(age)}")
    except ValueError as error:
        print(f"Invalid age: {error}")


# --------------------------------------------------------------------------
# Task 2: even / odd / zero
# --------------------------------------------------------------------------
def classify_number(n: int) -> str:
    """Return 'Zero', 'Even', or 'Odd'. Zero is checked first."""
    if n == 0:
        return "Zero"
    return "Even" if n % 2 == 0 else "Odd"


# --------------------------------------------------------------------------
# Task 3: compare two numbers
# --------------------------------------------------------------------------
def compare_numbers() -> None:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if a > b:
        print(f"{a:g} is greater.")
    elif b > a:
        print(f"{b:g} is greater.")
    else:
        print("Both are equal")


# --------------------------------------------------------------------------
# Task 4: password validation
# --------------------------------------------------------------------------
def check_password(password: str) -> list[str]:
    """Return a list of unmet requirements (empty list means valid)."""
    problems = []
    if len(password) < 8:
        problems.append("at least 8 characters")
    if not any(c.isupper() for c in password):
        problems.append("an uppercase letter")
    if not any(c.islower() for c in password):
        problems.append("a lowercase letter")
    if not any(c.isdigit() for c in password):
        problems.append("a digit")
    if not any(c in string.punctuation for c in password):
        problems.append("a special character (e.g. @, #, $)")
    return problems


def is_valid_password(password: str) -> bool:
    return not check_password(password)


# --------------------------------------------------------------------------
# Task 5: percentage -> grade
# --------------------------------------------------------------------------
def grade_for(percentage: float) -> str:
    """Return the letter grade for a percentage between 0 and 100."""
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"


def print_grade(percentage: float) -> None:
    try:
        print(f"{percentage:g}% -> Grade {grade_for(percentage)}")
    except ValueError as error:
        print(f"Invalid percentage: {error}")


# --------------------------------------------------------------------------
# Demo / tests
# --------------------------------------------------------------------------
def main() -> None:
    print("=== Task 1: age category ===")
    ask_age()
    for age, expected in [(5, "child"), (11, "child"), (12, "teenager"),
                          (17, "teenager"), (18, "adult"), (65, "adult"),
                          (66, "senior")]:
        assert age_category(age) == expected, age

    print("\n=== Task 2: even / odd / zero ===")
    for n in (0, 7, 10, -3):
        print(f"{n}: {classify_number(n)}")
    assert classify_number(0) == "Zero"
    assert classify_number(4) == "Even"
    assert classify_number(-3) == "Odd"

    print("\n=== Task 3: compare numbers ===")
    compare_numbers()

    print("\n=== Task 4: password check ===")
    for pw in ("Passw0rd@", "password", "SHORT1@", "NoDigits@@", "NoSpecial123"):
        missing = check_password(pw)
        status = "valid" if not missing else "missing " + ", ".join(missing)
        print(f"{pw!r}: {status}")
    assert is_valid_password("Passw0rd@")
    assert not is_valid_password("password")

    print("\n=== Task 5: grades ===")
    for score in (95, 90, 89.5, 80, 75, 60, 59.9, 0):
        print_grade(score)
    assert [grade_for(s) for s in (100, 90, 89, 80, 79, 70, 69, 60, 59)] == \
        ["A", "A", "B", "B", "C", "C", "D", "D", "F"]

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()