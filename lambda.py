"""Five exercises on functions, lambdas, recursion, and sorting."""

import timeit


# --------------------------------------------------------------------------
# Task 1: sum of two numbers
# --------------------------------------------------------------------------
def add(a: float, b: float) -> float:
    return a + b


# --------------------------------------------------------------------------
# Task 2: lambda returning the product of three numbers
# --------------------------------------------------------------------------
product3 = lambda x, y, z: x * y * z  # noqa: E731


# --------------------------------------------------------------------------
# Task 3: power function, then the lambda version
# --------------------------------------------------------------------------
def power(base: float, exponent: int) -> float:
    """Compute base ** exponent with a loop (integer exponents)."""
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result


power_lambda = lambda base, exponent: base ** exponent  # noqa: E731


# --------------------------------------------------------------------------
# Task 4: recursive vs iterative factorial
# --------------------------------------------------------------------------
def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def compare_factorials(n: int = 500, runs: int = 2000) -> None:
    t_rec = timeit.timeit(lambda: factorial_recursive(n), number=runs)
    t_iter = timeit.timeit(lambda: factorial_iterative(n), number=runs)
    print(f"n={n}, {runs} runs")
    print(f"  recursive: {t_rec:.4f}s")
    print(f"  iterative: {t_iter:.4f}s")
    print(f"  recursive is {t_rec / t_iter:.2f}x the iterative time")


# --------------------------------------------------------------------------
# Task 5: sort a list of dictionaries with a lambda key
# --------------------------------------------------------------------------
def sort_dicts(items: list[dict], key: str, descending: bool = False) -> list[dict]:
    """Return a new list sorted by ``key`` (original list is unchanged)."""
    return sorted(items, key=lambda item: item[key], reverse=descending)


# --------------------------------------------------------------------------
# Demo / tests
# --------------------------------------------------------------------------
def main() -> None:
    print("=== Task 1: add ===")
    for a, b in [(2, 3), (-4, 10), (2.5, 0.5), (0, 0)]:
        print(f"add({a}, {b}) = {add(a, b)}")
    assert add(2, 3) == 5 and add(-4, 10) == 6 and add(2.5, 0.5) == 3.0

    print("\n=== Task 2: lambda product of three ===")
    tests = [((2, 3, 4), 24), ((-2, 3, 4), -24), ((-2, -3, 4), 24),
             ((-2, -3, -4), -24), ((5, 0, 7), 0)]
    for args, expected in tests:
        print(f"product3{args} = {product3(*args)}")
        assert product3(*args) == expected

    print("\n=== Task 3: power (function vs lambda) ===")
    for base, exp in [(2, 10), (5, 0), (3, 3), (2, -2)]:
        print(f"{base}^{exp}: function={power(base, exp)}, lambda={power_lambda(base, exp)}")
        assert power(base, exp) == power_lambda(base, exp)

    print("\n=== Task 4: recursive vs iterative factorial ===")
    assert factorial_recursive(10) == factorial_iterative(10) == 3628800
    assert factorial_recursive(0) == factorial_iterative(0) == 1
    compare_factorials()

    print("\n=== Task 5: sort dictionaries with a lambda ===")
    people = [
        {"name": "Charlie", "age": 35},
        {"name": "alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    print("By age (asc):  ", [p["name"] for p in sort_dicts(people, "age")])
    print("By age (desc): ", [p["name"] for p in sort_dicts(people, "age", True)])
    print("By name (asc): ", [p["name"] for p in sort_dicts(people, "name")])
    assert [p["age"] for p in sort_dicts(people, "age")] == [25, 30, 35]
    assert [p["age"] for p in sort_dicts(people, "age", True)] == [35, 30, 25]

    # Case-insensitive name sort: alice comes first
    by_name_ci = sorted(people, key=lambda p: p["name"].lower())
    print("By name (case-insensitive):", [p["name"] for p in by_name_ci])

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()