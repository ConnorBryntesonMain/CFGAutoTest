import os
from typing import List, Dict, Any, Tuple, Callable

def write_test_file(target_path: str, functions: List[Tuple[str, Callable]], test_cases: Dict[str, List[Dict[str, Any]]]):
    """
    Generates a pytest file for the target module.
    
    Args:
        target_path: Path to the target python file.
        functions: List of (function_name, function_object) tuples.
        test_cases: Dictionary mapping function names to lists of input arguments.
    """
    target_filename = os.path.basename(target_path)
    module_name = os.path.splitext(target_filename)[0]
    test_filename = f"{module_name}_test.py"
    test_file_path = os.path.join(os.path.dirname(target_path), test_filename)
    
    with open(test_file_path, 'w') as f:
        f.write("import pytest\n")
        f.write(f"from {module_name} import *\n\n")
        
        for func_name, _ in functions:
            inputs = test_cases.get(func_name, [])
            if not inputs:
                continue
                
            f.write(f"@pytest.mark.parametrize('kwargs', [\n")
            for case in inputs:
                f.write(f"    {case},\n")
            f.write(f"])\n")
            
            f.write(f"def test_{func_name}(kwargs):\n")
            f.write(f"    # Generated test for {func_name}\n")
            f.write(f"    try:\n")
            f.write(f"        {func_name}(**kwargs)\n")
            f.write(f"    except Exception as e:\n")
            f.write(f"        pytest.fail(f'Function {func_name} raised exception: {{e}}')\n\n")
            
    print(f"Generated test file: {test_file_path}")
