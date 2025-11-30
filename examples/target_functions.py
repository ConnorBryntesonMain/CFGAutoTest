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

def solve_quadratic(a: float, b: float, c: float):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns a tuple of roots.
    """
    import math
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("Discriminant is negative, no real roots.")
        
    sqrt_d = math.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)
    return (root1, root2)

def process_order(quantity: int, price: float, member: bool):
    """
    Calculates the total price of an order.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > 100:
        raise ValueError("Quantity too large for a single order.")
    if price <= 0:
        raise ValueError("Price must be positive.")
        
    total = quantity * price
    if member:
        total *= 0.9 # 10% discount for members
        
    return total

def validate_username(username: str):
    """
    Validates a username.
    """
    if len(username) < 5:
        raise ValueError("Username too short.")
    if len(username) > 15:
        raise ValueError("Username too long.")
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric.")
    return True
