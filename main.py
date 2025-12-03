import argparse
import importlib.util
import sys
import os
import inspect
from typing import Callable, Any, List, Dict, Tuple, Optional
from src.cfg_generator import CFGLoader, CFG
from src.test_generator import TestGenerator
from src.file_writer import write_test_file, write_cfg_report

def load_module_from_path(path: str):
    spec = importlib.util.spec_from_file_location("target_module", path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules["target_module"] = module
        spec.loader.exec_module(module)
        return module
    return None

def parse_arguments_dict(func: Callable, args_str: str) -> Dict[str, Any]:
    """
    Parses a space-separated string of arguments into a dictionary matching the function signature.
    """
    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    raw_args = args_str.split()
    
    # Handle explicit empty string case if split returns empty but we have a string type param
    if not raw_args and len(params) == 1 and params[0].annotation == str:
        raw_args = [""]
        
    parsed_args = {}
    for i, param in enumerate(params):
        arg_val = None
        if i < len(raw_args):
            arg_str = raw_args[i]
            param_type = param.annotation
            try:
                if param_type == int:
                    arg_val = int(arg_str)
                elif param_type == float:
                    arg_val = float(arg_str)
                elif param_type == bool:
                    arg_val = arg_str.lower() == "true"
                else:
                    arg_val = arg_str
            except ValueError:
                arg_val = arg_str
        
        if arg_val is not None:
            parsed_args[param.name] = arg_val
            
    return parsed_args

def run_test_for_grammar(grammar_path: str, target_module: Any, count: int) -> Tuple[Optional[CFG], List[Dict[str, Any]]]:
    # Load CFG
    loader = CFGLoader()
    cfg = loader.load_from_file(grammar_path)
    
    if not cfg.target_function:
        print(f"Error: Grammar {grammar_path} does not specify a target function.")
        return None, []
        
    if not hasattr(target_module, cfg.target_function):
        print(f"Error: Target function '{cfg.target_function}' not found in module.")
        return None, []
        
    target_func = getattr(target_module, cfg.target_function)
    test_gen = TestGenerator()
    
    print(f"\n--- Generating {count} valid tests for {cfg.target_function} ---")
    
    valid_cases = []
    attempts = 0
    max_attempts = count * 50 # Allow many retries to find valid cases
    
    while len(valid_cases) < count and attempts < max_attempts:
        attempts += 1
        test_input_str = test_gen.generate_test_case(cfg)
        
        try:
            # Parse arguments
            args_dict = parse_arguments_dict(target_func, test_input_str)
            
            # Try executing to check validity
            # We assume "accepted" means it doesn't raise an exception
            target_func(**args_dict)
            
            # If successful, store it
            # We also store '_is_valid': True for the test file writer
            args_dict['_is_valid'] = True
            valid_cases.append(args_dict)
            print(f"  [Valid] '{test_input_str}'")
            
        except Exception:
            # If it raises an exception, it's not "accepted" in this context
            # So we ignore it and retry
            pass
            
    if len(valid_cases) < count:
        print(f"Warning: Could only generate {len(valid_cases)} valid cases after {attempts} attempts.")
        
    return cfg, valid_cases

def main():
    parser = argparse.ArgumentParser(description="CFG Auto Test Generator")
    parser.add_argument("target_file", help="Path to the python file containing functions to test")
    parser.add_argument("--grammar", help="Path to JSON grammar file or directory", required=True)
    parser.add_argument("--count", help="Number of test cases to generate per grammar", type=int, default=5)
    
    args = parser.parse_args()
    
    # Load target module
    target_module = load_module_from_path(args.target_file)
    if not target_module:
        print(f"Error: Could not load module {args.target_file}")
        return

    grammar_path = args.grammar
    grammar_files = []
    
    if os.path.isdir(grammar_path):
        files = [f for f in os.listdir(grammar_path) if f.endswith(".json")]
        files.sort()
        for f in files:
            grammar_files.append(os.path.join(grammar_path, f))
    else:
        grammar_files.append(grammar_path)
        
    if not grammar_files:
        print(f"No grammar files found in {grammar_path}")
        return

    all_test_cases = {}
    all_cfgs = {}
    functions_list = []
    
    for g_path in grammar_files:
        cfg, cases = run_test_for_grammar(g_path, target_module, args.count)
        if cfg and cases:
            func_name = cfg.target_function
            all_test_cases[func_name] = cases
            # Wrap CFG in a dict for the report writer (which expects param -> CFG)
            all_cfgs[func_name] = {"Global": cfg}
            
            # Add to functions list if not already there
            if not any(f[0] == func_name for f in functions_list):
                functions_list.append((func_name, getattr(target_module, func_name)))

    # Write test file
    if all_test_cases:
        write_test_file(args.target_file, functions_list, all_test_cases)
        
        # Run the generated tests to get output for the report
        import subprocess
        test_output = ""
        try:
            target_filename = os.path.basename(args.target_file)
            module_name = os.path.splitext(target_filename)[0]
            test_filename = f"{module_name}_test.py"
            test_file_path = os.path.join(os.path.dirname(args.target_file), test_filename)
            
            print(f"Running generated tests: {test_file_path}")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "-v", test_file_path],
                capture_output=True,
                text=True
            )
            test_output = result.stdout + "\n" + result.stderr
            if result.returncode == 0:
                print("All generated tests passed.")
            else:
                print("Some generated tests failed (unexpectedly).")
                
        except Exception as e:
            test_output = f"Error running tests: {e}"
            print(test_output)

        # Write Report
        write_cfg_report(args.target_file, all_cfgs, test_output)
    else:
        print("No valid test cases generated.")

if __name__ == "__main__":
    main()
