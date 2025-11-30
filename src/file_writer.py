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
            summary = _summarize_test_results(test_output)
            f.write("## Detected Bugs / Test Results\n\n")
            f.write(summary)
            f.write("\n\n<details>\n<summary>Raw Test Output</summary>\n\n```\n")
            f.write(test_output)
            f.write("\n```\n</details>\n")
                
    print(f"Generated CFG report: {report_file_path}")

def _summarize_test_results(output: str) -> str:
    """
    Parses pytest output and returns a markdown summary.
    """
    import re
    
    # Extract summary line
    summary_line_match = re.search(r'=+ (.*?) =+', output.splitlines()[-1])
    summary_line = summary_line_match.group(1) if summary_line_match else "Unknown Status"
    
    # Extract failures
    failures = []
    
    # Split output into blocks based on the separator line
    # Pytest failure blocks start with ____________ test_name ____________
    blocks = re.split(r'_{10,} (.*?) _{10,}', output)
    
    # The first block is usually setup/collection, subsequent blocks are failures
    # blocks[0] is pre-failure, blocks[1] is test name, blocks[2] is content, blocks[3] is test name...
    
    if len(blocks) > 1:
        for i in range(1, len(blocks), 2):
            test_name_full = blocks[i]
            content = blocks[i+1]
            
            # Parse test name (remove [kwargs...])
            test_name = test_name_full.split("[")[0]
            if "[" in test_name_full:
                 param = "[" + test_name_full.split("[", 1)[1]
                 test_name += param
            
            # Find error message (E   Error: ...)
            error_match = re.search(r'^E\s+(.*)$', content, re.MULTILINE)
            error_msg = error_match.group(1) if error_match else "Unknown Error"
            
            # Find line number (filename:line: ...)
            # Look for the line where the failure happened in the test file
            # usually: examples/target_functions_test.py:51: Failed
            line_match = re.search(r'target_functions_test\.py:(\d+):', content)
            line_num = line_match.group(1) if line_match else "?"
            
            failures.append((test_name, line_num, error_msg))

    if not failures:
        # Fallback to simple parsing if blocks didn't work (e.g. short output)
        if "FAILED" in output:
             return f"**Status**: {summary_line}\n\nTests failed but detailed parsing failed. See raw output."
        return f"**Status**: {summary_line}\n\nAll tests passed!"
        
    table = f"**Status**: {summary_line}\n\n"
    table += "| Test Case | Line | Failure Reason |\n"
    table += "| :--- | :--- | :--- |\n"
    
    for name, line, reason in failures:
        table += f"| `{name}` | {line} | {reason} |\n"
        
    return table
