# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-kNSYkd78PA03d95qH5Dn0-dcS4r45OO
"""

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Testing code
def test_calculator():
    calculator = Calculator()

    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 3) == 6
    assert calculator.divide(6, 2) == 3

    try:
        calculator.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

# Perfect Pylint Score Python Script

def calculate_sum(number_1, number_2):
    """
    This function calculates the sum of two numbers.
    """
    result = number_1 + number_2
    return result

if __name__ == "__main__":
    number_1 = 5
    number_2 = 10
    print(f"The sum of {number_1} and {number_2} is: {calculate_sum(number_1, number_2)}")

