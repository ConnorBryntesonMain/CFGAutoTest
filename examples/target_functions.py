def add(a: int, b: int):
    """Adds two integers."""
    return a + b

def divide(a: float, b: float):
    """Divides two floats."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name: str):
    """Greets a user."""
    return f"Hello, {name}!"

def check_age(age: int):
    """Checks if age is valid."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age too high")
    return True
