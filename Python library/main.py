# example_usage.py

from mymathlib import add, subtract, multiply, divide, modulo, power, is_even, absolute_value
from mymathlib import __version__

def main():
    print(f"MyMathLib version: {__version__}")

    result_add = add(5, 3)
    print(f"Addition: {result_add}")

    result_subtract = subtract(8, 2)
    print(f"Subtraction: {result_subtract}")

    result_multiply = multiply(4, 6)
    print(f"Multiplication: {result_multiply}")

    try:
        result_divide = divide(10, 2)
        print(f"Division: {result_divide}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    result_modulo = modulo(10, 3)
    print(f"Modulo: {result_modulo}")

    result_power = power(2, 3)
    print(f"Power: {result_power}")

    number = 6
    print(f"Is {number} even? {is_even(number)}")

    number = -8
    print(f"Absolute value of {number}: {absolute_value(number)}")

if __name__ == "__main__":
    main()
