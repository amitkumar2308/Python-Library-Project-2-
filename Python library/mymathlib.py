# mymathlib/__init__.py

__version__ = "1.0.0"



# mymathlib/operations.py

def add(a, b):
    """
    Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a: The first number (minuend).
        b: The second number (subtrahend).

    Returns:
        The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together.

    Args:
        a: The first number (multiplicand).
        b: The second number (multiplier).

    Returns:
        The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a: The first number (dividend).
        b: The second number (divisor).

    Returns:
        The quotient of a and b.
    """
    return a / b

def modulo(a, b):
    """
    Returns the remainder of dividing the first number by the second.

    Args:
        a: The first number (dividend).
        b: The second number (divisor).

    Returns:
        The remainder of a divided by b.
    """
    return a % b

def power(a, b):
    """
    Raises the first number to the power of the second.

    Args:
        a: The base number.
        b: The exponent.

    Returns:
        The base raised to the power of the exponent.
    """
    return a ** b

# Additional functions for advanced calculations can be added here

def is_even(number):
    """
    Checks if a number is even.

    Args:
        number: The number to check.

    Returns:
        True if the number is even, False otherwise.
    """
    return number % 2 == 0

def absolute_value(number):
    """
    Returns the absolute value of a number.

    Args:
        number: The number.

    Returns:
        The absolute value of the number.
    """
    return abs(number)
