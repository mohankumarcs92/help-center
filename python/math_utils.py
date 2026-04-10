# math_utils.py - Mathematical utility functions
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0
def factorial(n): if n == 0:
return 1 result = 1
for i in range(1, n + 1): result *= i
return result