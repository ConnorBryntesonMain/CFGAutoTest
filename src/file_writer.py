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
                # Filter out _is_valid for the kwargs list, but keep it for logic?
                # No, we need to pass it to the test function or handle it here.
                # Better: pass it as part of kwargs and pop it in the test function.
                f.write(f"    {case},\n")
            f.write(f"])\n")
            
            f.write(f"def test_{func_name}(kwargs):\n")
            f.write(f"    # Generated test for {func_name}\n")
            f.write(f"    is_valid = kwargs.pop('_is_valid', True)\n")
            f.write(f"    \n")
            f.write(f"    if is_valid:\n")
            f.write(f"        try:\n")
            f.write(f"            {func_name}(**kwargs)\n")
            f.write(f"        except Exception as e:\n")
            f.write(f"            pytest.fail(f'Function {func_name} raised exception on valid input: {{e}}')\n")
            f.write(f"    else:\n")
            f.write(f"        # Expect failure\n")
            f.write(f"        with pytest.raises(Exception):\n")
            f.write(f"            {func_name}(**kwargs)\n\n")
            
    print(f"Generated test file: {test_file_path}")

def write_cfg_report(target_path: str, cfgs: Dict[str, Dict[str, Any]], test_output: str = None):
    """
    Generates a markdown report of the generated CFGs and test results.
    
    Args:
        target_path: Path to the target python file.
        cfgs: Dictionary mapping function names to parameter CFGs.
        test_output: Output from running the tests (optional).
    """
    target_filename = os.path.basename(target_path)
    module_name = os.path.splitext(target_filename)[0]
    report_filename = f"{module_name}_cfg_report.md"
    report_file_path = os.path.join(os.path.dirname(target_path), report_filename)
    
    with open(report_file_path, 'w') as f:
        f.write(f"# CFG Report for {module_name}\n\n")
        
        for func_name, param_cfgs in cfgs.items():
            f.write(f"## Function: `{func_name}`\n\n")
            
            for param_name, cfg in param_cfgs.items():
                f.write(f"### Parameter: `{param_name}`\n")
                f.write(f"- **Start Symbol**: `{cfg.start_symbol}`\n")
                f.write(f"- **Reasoning**: {cfg.reasoning}\n")
                f.write(f"- **Productions**:\n")
                for symbol, prods in cfg.productions.items():
                    for prod in prods:
                        f.write(f"    - `{symbol} -> {prod}`\n")
                f.write("\n")
        
        if test_output:
            f.write("## Detected Bugs / Test Results\n\n")
            f.write("```\n")
            f.write(test_output)
            f.write("\n```\n")
                
    print(f"Generated CFG report: {report_file_path}")
