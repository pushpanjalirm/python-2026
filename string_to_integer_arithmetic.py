def main() -> None:
    """Convert an input string to an integer and do addition/subtraction."""
    number_text = input("Enter a string containing an integer: ")

    try:
        number = int(number_text)
        other_number = int(input("Enter another integer: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return

    print("Converted integer:", number)
    print("Addition:", number + other_number)
    print("Subtraction:", number - other_number)


if __name__ == "__main__":
    main()
