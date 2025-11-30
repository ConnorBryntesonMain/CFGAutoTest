import random
from typing import List, Any, Dict
from .cfg_generator import CFG

class TestGenerator:
    """
    Generates test inputs based on a Context Free Grammar.
    """
    
    def generate_inputs(self, cfgs: Dict[str, CFG], count: int = 5) -> List[Dict[str, Any]]:
        """
        Generates a list of test cases, where each test case is a dictionary
        mapping parameter names to generated values.
        
        Args:
            cfgs: Dictionary of CFGs for each parameter.
            count: Number of test cases to generate.
            
        Returns:
            List of dictionaries representing function arguments.
        """
        test_cases = []
        for _ in range(count):
            case = {}
            for param, cfg in cfgs.items():
                case[param] = self._generate_from_cfg(cfg)
            test_cases.append(case)
        return test_cases

    def _generate_from_cfg(self, cfg: CFG) -> Any:
        # Simple generation: pick a random production from start symbol
        # Since our current CFG implementation is flat (S -> val1 | val2), this is sufficient.
        # For recursive grammars, we would need a recursive generator.
        
        production = random.choice(cfg.productions[cfg.start_symbol])
        
        # Post-processing to convert string representation back to python types
        # This is a simplification. Ideally the CFG generates the string representation
        # and we eval it or parse it.
        try:
            # Handle quoted strings
            if production.startswith('"') and production.endswith('"'):
                return production[1:-1]
            # Handle booleans
            if production == "True": return True
            if production == "False": return False
            # Handle numbers
            if '.' in production:
                return float(production)
            return int(production)
        except ValueError:
            return production
