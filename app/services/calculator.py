import math
import requests


class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number")
        return math.sqrt(a)

    def generate_random_string(self, length: int) -> str:
        # Using http instead of https to avoid a registration in random.org site
        url = f"http://www.random.org/strings/?num=1&len={length}&digits=on&upperalpha=on&loweralpha=on&unique=off&format=plain"

        response = requests.get(url)

        if response.status_code == 200:
            return response.text.strip()
        else:
            raise Exception("Error in external provider")
