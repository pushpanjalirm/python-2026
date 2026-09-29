"""Five exercises on dictionaries and sets."""


def show(chars: set[str]) -> str:
    """Format a set of characters in sorted order so output is stable."""
    return "{" + ", ".join(repr(c) for c in sorted(chars)) + "}"


# --------------------------------------------------------------------------
# Task 1: count occurrences of each character
# --------------------------------------------------------------------------
def count_characters(text: str) -> dict[str, int]:
    """Count every character (case-sensitive, spaces included)."""
    counts: dict[str, int] = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


# --------------------------------------------------------------------------
# Task 2: union and intersection of the unique characters in two strings
# --------------------------------------------------------------------------
def union_and_intersection(first: str, second: str) -> None:
    set_a, set_b = set(first), set(second)
    print(f"Unique in {first!r}:  {show(set_a)}")
    print(f"Unique in {second!r}: {show(set_b)}")
    print("Union:       ", show(set_a | set_b))
    print("Intersection:", show(set_a & set_b))


# --------------------------------------------------------------------------
# Task 3: key with the largest value
# --------------------------------------------------------------------------
def key_of_max_value(data: dict) -> object:
    """Return the key with the largest value.

    On a tie, the key that appears first in the dictionary is returned.
    """
    if not data:
        raise ValueError("Dictionary is empty.")
    best_key = None
    best_value = None
    for key, value in data.items():
        if best_value is None or value > best_value:
            best_key, best_value = key, value
    return best_key


# --------------------------------------------------------------------------
# Task 4: merge two dictionaries, summing values for shared keys
# --------------------------------------------------------------------------
def merge_sum(first: dict[int, int], second: dict[int, int]) -> dict[int, int]:
    merged = dict(first)  # copy, so the inputs are not modified
    for key, value in second.items():
        merged[key] = merged.get(key, 0) + value
    return merged


# --------------------------------------------------------------------------
# Task 5: set operations on the characters of two strings
# --------------------------------------------------------------------------
def string_set_operations(first: str, second: str) -> dict[str, set[str]]:
    a, b = set(first), set(second)
    return {
        "intersection": a & b,
        "symmetric_difference": a ^ b,
        "difference (first - second)": a - b,
    }


# --------------------------------------------------------------------------
# Demo / tests
# --------------------------------------------------------------------------
def main() -> None:
    print("=== Task 1: character counts ===")
    counts = count_characters("hello world")
    print(counts)
    assert counts == {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}
    assert count_characters("") == {}
    assert count_characters("aAa") == {"a": 2, "A": 1}

    print("\n=== Task 2: union and intersection ===")
    union_and_intersection("apple", "grape")
    assert set("apple") | set("grape") == set("aplegr")
    assert set("apple") & set("grape") == set("ape")

    print("\n=== Task 3: key with the largest value ===")
    scores = {"alice": 82, "bob": 95, "carol": 78}
    print(key_of_max_value(scores))
    assert key_of_max_value(scores) == "bob"
    assert key_of_max_value({"a": -5, "b": -2}) == "b"       # negatives
    assert key_of_max_value({"x": 3, "y": 3}) == "x"         # tie -> first
    try:
        key_of_max_value({})
    except ValueError as error:
        print("Empty dict:", error)

    print("\n=== Task 4: merge and sum ===")
    d1 = {1: 10, 2: 20, 3: 30}
    d2 = {2: 5, 3: 15, 4: 40}
    merged = merge_sum(d1, d2)
    print(merged)
    assert merged == {1: 10, 2: 25, 3: 45, 4: 40}
    assert d1 == {1: 10, 2: 20, 3: 30}  # original untouched

    print("\n=== Task 5: set operations on two strings ===")
    results = string_set_operations("python", "typhoon")
    for name, chars in results.items():
        print(f"{name}: {show(chars)}")
    assert results["intersection"] == set("pyhton")
    assert results["symmetric_difference"] == set()
    assert results["difference (first - second)"] == set()

    results = string_set_operations("hello", "world")
    for name, chars in results.items():
        print(f"{name}: {show(chars)}")
    assert results["intersection"] == {"l", "o"}
    assert results["symmetric_difference"] == set("hewrd")
    assert results["difference (first - second)"] == set("he")

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()