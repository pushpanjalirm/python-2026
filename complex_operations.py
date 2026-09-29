def complex_operations(a: complex, b: complex) -> dict[str, complex]:
    """Return the results of basic operations on two complex numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
    }


if __name__ == "__main__":
    first_number = complex(input("Enter the first complex number (for example, 2+3j): "))
    second_number = complex(input("Enter the second complex number (for example, 1-1j): "))
    results = complex_operations(first_number, second_number)
    print(results)
