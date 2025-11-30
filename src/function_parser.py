import inspect
from typing import Callable, Dict, Any, get_type_hints

def infer_bounds(func: Callable) -> Dict[str, Any]:
    """
    Infers parameter bounds from a function's type hints.
    
    Args:
        func: The target function to inspect.
        
    Returns:
        A dictionary mapping parameter names to inferred bounds.
    """
    bounds = {}
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)
    
    for param_name, param in sig.parameters.items():
        if param_name == 'self' or param_name == 'cls':
            continue
            
        param_type = type_hints.get(param_name, Any)
        
        if param_type == int:
            # Default bounds for integers
            bounds[param_name] = {"type": "int", "min": -100, "max": 100}
        elif param_type == float:
             # Default bounds for floats
            bounds[param_name] = {"type": "float", "min": -100.0, "max": 100.0}
        elif param_type == str:
            # Default bounds for strings
            bounds[param_name] = {"type": "str", "max_length": 10, "charset": "alphanumeric"}
        elif param_type == bool:
            bounds[param_name] = {"type": "bool"}
        else:
            # Fallback for unknown types
            bounds[param_name] = {"type": "unknown"}
            
    return bounds
