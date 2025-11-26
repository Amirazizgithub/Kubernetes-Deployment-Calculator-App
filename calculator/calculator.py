# write a python code to implement a simple calculator that can perform addition, subtraction, multiplication, and division operations.

class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, num1: int, num2: int) -> int:
        return num1 + num2

    def subtract(self, num1: int, num2: int) -> int:
        return num1 - num2

    def multiply(self, num1: int, num2: int) -> int:
        return num1 * num2

    def divide(self, num1: int, num2: int) -> int:
        return int(num1 / num2)