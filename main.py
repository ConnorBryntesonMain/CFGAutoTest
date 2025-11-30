import argparse
import importlib.util
import sys
import os
from typing import Callable
from src.config_loader import load_config
from src.function_parser import infer_bounds
from src.cfg_generator import CFGGenerator
from src.test_generator import TestGenerator

def load_module_from_path(path: str):
    spec = importlib.util.spec_from_file_location("target_module", path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules["target_module"] = module
        spec.loader.exec_module(module)
        return module
    return None

def main():
    parser = argparse.ArgumentParser(description="CFG Auto Test Generator")
    parser.add_argument("target_file", help="Path to the python file containing functions to test")
    parser.add_argument("--config", help="Path to JSON config file with bounds", default=None)
    parser.add_argument("--function", help="Specific function to test (default: all)", default=None)
    
    args = parser.parse_args()
    
    # Load target module
    target_module = load_module_from_path(args.target_file)
    if not target_module:
        print(f"Error: Could not load module {args.target_file}")
        return

    # Load bounds
    file_bounds = {}
    if args.config:
        try:
            file_bounds = load_config(args.config)
        except Exception as e:
            print(f"Error loading config: {e}")
            return

    # Identify functions to test
    functions_to_test = []
    if args.function:
        if hasattr(target_module, args.function):
            functions_to_test.append((args.function, getattr(target_module, args.function)))
        else:
            print(f"Error: Function {args.function} not found in {args.target_file}")
            return
    else:
        for name, obj in vars(target_module).items():
            if callable(obj) and not name.startswith("_"):
                functions_to_test.append((name, obj))

    cfg_gen = CFGGenerator()
    test_gen = TestGenerator()

    # Generate Tests
    all_test_cases = {}
    for func_name, func in functions_to_test:
        print(f"Processing function: {func_name}")
        
        # Determine bounds: Config > Inferred
        bounds = file_bounds.get(func_name)
        if not bounds:
            print(f"  No config found, inferring bounds...")
            bounds = infer_bounds(func)
            
        # Generate CFG
        cfgs = cfg_gen.from_bounds(bounds)
        
        # Generate Tests
        inputs = test_gen.generate_inputs(cfgs, count=5)
        all_test_cases[func_name] = inputs

    # Write test file
    from src.file_writer import write_test_file
    write_test_file(args.target_file, functions_to_test, all_test_cases)

if __name__ == "__main__":
    main()
