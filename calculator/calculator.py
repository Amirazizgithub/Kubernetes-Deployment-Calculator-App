import math

class ScientificCalculator:
    def __init__(self) -> None:
        pass

    def add(self, num1: float, num2: float) -> float:
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        return num1 * num2

    def divide(self, num1: float, num2: float) -> float:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

    def power(self, base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    def sqrt(self, num: float) -> float:
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(num)

    def log(self, num: float) -> float:
        if num <= 0:
            raise ValueError("Logarithm defined only for positive numbers")
        return math.log10(num)

    def ln(self, num: float) -> float:
        if num <= 0:
            raise ValueError("Logarithm defined only for positive numbers")
        return math.log(num)

    def sin(self, angle_degrees: float) -> float:
        return math.sin(math.radians(angle_degrees))

    def cos(self, angle_degrees: float) -> float:
        return math.cos(math.radians(angle_degrees))

    def tan(self, angle_degrees: float) -> float:
        return math.tan(math.radians(angle_degrees))

    def factorial(self, num: float) -> int:
        if num < 0 or not num.is_integer():
             raise ValueError("Factorial only defined for non-negative integers")
        return math.factorial(int(num))