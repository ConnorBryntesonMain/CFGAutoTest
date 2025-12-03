import json
from typing import Dict, List, Any

class CFG:
    def __init__(self, start_symbol: str, productions: Dict[str, List[str]], target_function: str = ""):
        self.start_symbol = start_symbol
        self.productions = productions
        self.target_function = target_function

    def __repr__(self):
        return f"CFG(target={self.target_function}, start={self.start_symbol}, productions={self.productions})"

class CFGLoader:
    """
    Loads a Context Free Grammar from a JSON file.
    """
    
    def load_from_file(self, file_path: str) -> CFG:
        """
        Loads the CFG from the specified JSON file.
        
        Args:
            file_path: Path to the JSON file containing the grammar.
            
        Returns:
            A CFG object.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            return CFG(
                start_symbol=data.get("start_symbol", "S"),
                productions=data.get("productions", {}),
                target_function=data.get("target_function", "")
            )
        except Exception as e:
            print(f"Error loading CFG from {file_path}: {e}")
            return CFG("Error", {})

