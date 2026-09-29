"""Five exercises on lists, list comprehensions, and matrices."""

from typing import Any


# --------------------------------------------------------------------------
# Task 1: print a list in reverse order
# --------------------------------------------------------------------------
def reversed_list(numbers: list[int]) -> list[int]:
    """Return a reversed copy (the original list is unchanged)."""
    return numbers[::-1]


# --------------------------------------------------------------------------
# Task 2: cubes of numbers from 1 to 10 that are divisible by 2
# --------------------------------------------------------------------------
even_cubes = [n ** 3 for n in range(1, 11) if n % 2 == 0]


# --------------------------------------------------------------------------
# Task 3: merge two lists, remove duplicates, sort descending
# --------------------------------------------------------------------------
def merge_unique_descending(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a + b), reverse=True)


# --------------------------------------------------------------------------
# Task 4: flatten a nested list
# --------------------------------------------------------------------------
def flatten_one_level(nested: list[list[Any]]) -> list[Any]:
    """Flatten a list of lists using a list comprehension."""
    return [item for sublist in nested for item in sublist]


def flatten_deep(nested: list[Any]) -> list[Any]:
    """Flatten any depth of nesting: a loop plus a comprehension.

    Elements that are not lists are kept as they are; sublists are
    flattened recursively.
    """
    flat = []
    for element in nested:
        if isinstance(element, list):
            flat.extend([item for item in flatten_deep(element)])
        else:
            flat.append(element)
    return flat


# --------------------------------------------------------------------------
# Task 5: matrix multiplication with lists of lists
# --------------------------------------------------------------------------
def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Return the matrix product a x b.

    a must be m x n and b must be n x p; the result is m x p.
    """
    if not a or not b or not a[0] or not b[0]:
        raise ValueError("Matrices must not be empty.")
    if any(len(row) != len(a[0]) for row in a) or any(len(row) != len(b[0]) for row in b):
        raise ValueError("All rows in a matrix must have the same length.")
    if len(a[0]) != len(b):
        raise ValueError(
            f"Cannot multiply {len(a)}x{len(a[0])} by {len(b)}x{len(b[0])}: "
            "columns of the first must equal rows of the second."
        )

    rows, inner, cols = len(a), len(b), len(b[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i][j] += a[i][k] * b[k][j]
    return result


# --------------------------------------------------------------------------
# Demo / tests
# --------------------------------------------------------------------------
def main() -> None:
    print("=== Task 1: reverse a list ===")
    numbers = [3, 8, 1, 9, 4]
    print("Original:", numbers)
    print("Reversed:", reversed_list(numbers))
    assert reversed_list(numbers) == [4, 9, 1, 8, 3]
    assert numbers == [3, 8, 1, 9, 4]

    print("\n=== Task 2: cubes of even numbers 1-10 ===")
    print(even_cubes)
    assert even_cubes == [8, 64, 216, 512, 1000]

    print("\n=== Task 3: merge, dedupe, sort descending ===")
    a, b = [5, 1, 3, 3, 9], [3, 7, 1, 10]
    merged = merge_unique_descending(a, b)
    print(f"{a} + {b} -> {merged}")
    assert merged == [10, 9, 7, 5, 3, 1]

    print("\n=== Task 4: flatten a nested list ===")
    grid = [[1, 2], [3], [4, 5, 6]]
    print("One level:", flatten_one_level(grid))
    deep = [1, [2, [3, [4, 5]], 6], [], 7]
    print("Deep:     ", flatten_deep(deep))
    assert flatten_one_level(grid) == [1, 2, 3, 4, 5, 6]
    assert flatten_deep(deep) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten_deep([]) == []

    print("\n=== Task 5: matrix multiplication ===")
    m1 = [[1, 2, 3],
          [4, 5, 6]]          # 2x3
    m2 = [[7, 8],
          [9, 10],
          [11, 12]]           # 3x2
    product = matrix_multiply(m1, m2)
    for row in product:
        print(row)
    assert product == [[58, 64], [139, 154]]

    identity = [[1, 0], [0, 1]]
    assert matrix_multiply(product, identity) == product

    try:
        matrix_multiply(m1, m1)  # 2x3 times 2x3 is invalid
    except ValueError as error:
        print("Error:", error)

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()