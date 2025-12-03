import os
import subprocess
import sys

def verify_grammars():
    grammar_dir = "examples/grammars"
    target_file = "examples/target_functions.py"
    
    if not os.path.exists(grammar_dir):
        print(f"Directory {grammar_dir} does not exist.")
        return

    files = [f for f in os.listdir(grammar_dir) if f.endswith(".json")]
    
    for grammar_file in files:
        grammar_path = os.path.join(grammar_dir, grammar_file)
        print(f"--- Testing {grammar_file} ---")
        
        cmd = [sys.executable, "main.py", target_file, "--grammar", grammar_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
        print("\n")

if __name__ == "__main__":
    verify_grammars()
