def bitwise_operations(first: int, second: int) -> dict[str, int]:
    """Return bitwise operations for two integers.

    NOT and both shifts are applied to ``first``; the shifts use 2 positions.
    """
    return {
        "and": first & second,
        "or": first | second,
        "xor": first ^ second,
        "not_first": ~first,
        "left_shift_first_by_2": first << 2,
        "right_shift_first_by_2": first >> 2,
    }


if __name__ == "__main__":
    results = bitwise_operations(10, 6)
    for operation, result in results.items():
        print(f"{operation}: {result}")
