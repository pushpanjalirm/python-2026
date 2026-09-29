# lab1/working.py
"""Write a program that accepts two numbers from the command line and
performs addition, subtraction, multiplication, division, modulus, and
exponentiation. Output all the results."""

# Ask the user for two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform the operations
add = a + b
sub = a - b
mul = a * b
mod = a % b

# Output all the results
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Modulus:", mod)
