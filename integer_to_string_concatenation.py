"""Solutions for five Python conversion, merging, and class exercises."""

from copy import deepcopy
from typing import Any, Union


# Question 1: Take a string of numbers, convert it to an integer, and perform
# addition and subtraction using another integer.
def string_to_integer_arithmetic(
    number_text: str, other_number: int
) -> tuple[int, int, int]:
    """Return the converted integer, its sum, and its difference."""
    number = int(number_text)
    return number, number + other_number, number - other_number


# Question 2: Convert an integer to a string, concatenate it with another
# string, and print the result.
def concatenate_integer_with_string(number: int, text: str) -> str:
    """Convert an integer to text and append another string."""
    return str(number) + text


# Question 3: Convert an input value to float if it is an integer; otherwise,
# keep the value unchanged.
def convert_integer_to_float_if_needed(value: Any) -> Any:
    """Convert integers to floats, leaving all other values unchanged."""
    if isinstance(value, int) and not isinstance(value, bool):
        return float(value)
    return value


# Question 4: Merge two nested dictionaries. In case of conflict, values from
# the second dictionary overwrite values from the first dictionary.
def merge_nested_dictionaries(
    first: dict[str, Any], second: dict[str, Any]
) -> dict[str, Any]:
    """Return a recursive merge without modifying either input dictionary."""
    merged = deepcopy(first)

    for key, second_value in second.items():
        first_value = merged.get(key)
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            merged[key] = merge_nested_dictionaries(first_value, second_value)
        else:
            merged[key] = deepcopy(second_value)

    return merged


# Question 5: Create CustomNumber to store a numeric value and support
# conversion to integer, float, and string. Add methods and test the class.
class CustomNumber:
    """Store an integer or float and provide explicit conversion methods."""

    def __init__(self, value: Union[int, float]) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("CustomNumber requires an integer or float")
        self.value = value

    def to_integer(self) -> int:
        """Return the value converted to an integer."""
        return int(self.value)

    def to_float(self) -> float:
        """Return the value converted to a float."""
        return float(self.value)

    def to_string(self) -> str:
        """Return the value converted to a string."""
        return str(self.value)

    def __int__(self) -> int:
        return self.to_integer()

    def __float__(self) -> float:
        return self.to_float()

    def __str__(self) -> str:
        return self.to_string()


def main() -> None:
    """Run interactive examples and checks for all five exercises."""
    print("Question 1: Convert a numeric string and do arithmetic")
    number_text = input("Enter a string containing an integer: ")
    try:
        other_number = int(input("Enter another integer: "))
        number, total, difference = string_to_integer_arithmetic(
            number_text, other_number
        )
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return
    print("Converted integer:", number)
    print("Addition:", total)
    print("Subtraction:", difference)

    print("\nQuestion 2: Convert an integer to a string and concatenate")
    try:
        concatenation_number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return
    text = input("Enter another string: ")
    concatenated = concatenate_integer_with_string(concatenation_number, text)
    print("Result:", concatenated)

    print("\nQuestion 3: Convert integers to floats, keep other types unchanged")
    for value in (10, 3.5, "hello", True):
        converted = convert_integer_to_float_if_needed(value)
        print(f"{value!r} -> {converted!r} ({type(converted).__name__})")
    assert convert_integer_to_float_if_needed(10) == 10.0
    assert convert_integer_to_float_if_needed("hello") == "hello"
    assert convert_integer_to_float_if_needed(True) is True

    print("\nQuestion 4: Merge nested dictionaries")
    first = {"user": {"name": "Ava", "age": 20}, "active": True}
    second = {"user": {"age": 21, "city": "Seattle"}, "role": "admin"}
    merged = merge_nested_dictionaries(first, second)
    print("Merged dictionary:", merged)
    assert merged == {
        "user": {"name": "Ava", "age": 21, "city": "Seattle"},
        "active": True,
        "role": "admin",
    }
    assert first["user"]["age"] == 20

    print("\nQuestion 5: Test CustomNumber conversions")
    custom_number = CustomNumber(12.75)
    assert custom_number.to_integer() == 12
    assert custom_number.to_float() == 12.75
    assert custom_number.to_string() == "12.75"
    assert int(custom_number) == 12
    assert float(custom_number) == 12.75
    assert str(custom_number) == "12.75"
    print("Integer:", int(custom_number))
    print("Float:", float(custom_number))
    print("String:", str(custom_number))
    print("All CustomNumber conversion checks passed.")


if __name__ == "__main__":
    main()
