"""Five exercises on loops, nested loops, and generators."""

from collections.abc import Iterator


# --------------------------------------------------------------------------
# Task 1: sum of even numbers from 1 to 100 (for loop)
# --------------------------------------------------------------------------
def sum_of_evens(limit: int = 100) -> int:
    total = 0
    for number in range(1, limit + 1):
        if number % 2 == 0:
            total += number
    return total


# --------------------------------------------------------------------------
# Task 2: factorial using a while loop
# --------------------------------------------------------------------------
def factorial(n: int) -> int:
    """Return n! computed with a while loop (0! is 1)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    counter = n
    while counter > 1:
        result *= counter
        counter -= 1
    return result


# --------------------------------------------------------------------------
# Task 3: keep asking for numbers until a negative one is entered
# --------------------------------------------------------------------------
def sum_positive_until_negative() -> None:
    total = 0.0
    while True:
        text = input("Enter a number (negative to stop): ")
        try:
            number = float(text)
        except ValueError:
            print("Not a number, try again.")
            continue
        if number < 0:
            break
        total += number
    print(f"Sum of positive numbers: {total:g}")


# --------------------------------------------------------------------------
# Task 4: primes below n using a nested loop
# --------------------------------------------------------------------------
def primes_below(n: int) -> list[int]:
    primes = []
    for candidate in range(2, n):
        is_prime = True
        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


# --------------------------------------------------------------------------
# Task 5: Fibonacci generator
# --------------------------------------------------------------------------
def fibonacci_up_to(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers that are <= ``limit``."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# --------------------------------------------------------------------------
# Demo / tests
# --------------------------------------------------------------------------
def main() -> None:
    print("=== Task 1: sum of evens 1-100 ===")
    result = sum_of_evens()
    print(result)
    assert result == 2550

    print("\n=== Task 2: factorial (while loop) ===")
    for n in (0, 1, 5, 10):
        print(f"{n}! = {factorial(n)}")
    assert factorial(5) == 120 and factorial(0) == 1
    try:
        factorial(-1)
    except ValueError as error:
        print("factorial(-1):", error)

    print("\n=== Task 3: sum until negative ===")
    sum_positive_until_negative()

    print("\n=== Task 4: primes below n ===")
    print(primes_below(30))
    assert primes_below(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes_below(2) == []

    print("\n=== Task 5: Fibonacci generator ===")
    print(list(fibonacci_up_to(100)))
    assert list(fibonacci_up_to(20)) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list(fibonacci_up_to(0)) == [0]

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()