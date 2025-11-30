import json
import os
from typing import Dict, Any

def load_config(path: str) -> Dict[str, Any]:
    """
    Loads the JSON configuration file containing function bounds.
    
    Args:
        path: Path to the JSON config file.
        
    Returns:
        A dictionary mapping function names to their parameter bounds.
        
    Raises:
        FileNotFoundError: If the config file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found: {path}")
        
    with open(path, 'r') as f:
        return json.load(f)
