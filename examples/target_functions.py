def add(a: int, b: int):
    """Adds two integers."""
    if not (-100 <= a <= 100 and -100 <= b <= 100):
        raise ValueError("Inputs out of range")
    return a + b

def divide(a: float, b: float):
    """Divides two floats."""
    if not (-100.0 <= a <= 100.0 and -100.0 <= b <= 100.0):
        raise ValueError("Inputs out of range")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name: str):
    """Greets a user."""
    if len(name) < 1 or len(name) > 5:
        raise ValueError("Name length invalid")
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
    import cmath
    if not (-10.0 <= a <= 10.0 and -10.0 <= b <= 10.0 and -10.0 <= c <= 10.0):
        raise ValueError("Coefficients out of range")
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    # Use cmath.sqrt to handle negative discriminant
    sqrt_d = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)
    return (root1, root2)

def process_order(quantity: int, price: float, member: bool):
    """
    Calculates the total price of an order.
    """
    if not isinstance(member, bool):
        raise TypeError("Member must be a boolean.")
        
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > 100:
        raise ValueError("Quantity too large for a single order.")
    if price <= 0:
        raise ValueError("Price must be positive.")
    if price > 1000.0:
        raise ValueError("Price too high.")
        
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
