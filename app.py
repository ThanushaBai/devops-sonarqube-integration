"""Sample Python application for demonstrating SonarQube Cloud analysis.

This module provides basic arithmetic utility functions used to showcase
static code analysis via SonarQube Cloud and GitHub Actions CI/CD.
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the divisor (b) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exponent: int) -> int:
    """Return base raised to the power of exponent."""
    return base ** exponent


def average(numbers: list) -> float:
    """Return the average of a list of numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)


def is_even(number: int) -> bool:
    """Return True if the given number is even, otherwise False."""
    return number % 2 == 0


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main() -> None:
    """Run a quick demonstration of the utility functions."""
    print("Add:", add(2, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(6, 7))
    print("Divide:", divide(20, 4))
    print("Power:", power(2, 8))
    print("Average:", average([10, 20, 30, 40]))
    print("Is even (7):", is_even(7))
    print("Factorial (5):", factorial(5))


if __name__ == "__main__":
    main()
