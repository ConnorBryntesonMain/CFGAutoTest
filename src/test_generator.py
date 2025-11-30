import random
from typing import List, Any, Dict
from .cfg_generator import CFG

class TestGenerator:
    """
    Generates test inputs based on a Context Free Grammar.
    """
    
    def generate_inputs(self, cfgs: Dict[str, CFG], count: int = 5, invalid_cfgs: Dict[str, CFG] = None) -> List[Dict[str, Any]]:
        """
        Generates a list of test cases.
        
        Args:
            cfgs: Dictionary of CFGs for valid parameters.
            count: Number of test cases to generate.
            invalid_cfgs: Dictionary of CFGs for invalid parameters (optional).
            
        Returns:
            List of dictionaries representing function arguments, with an added key '_is_valid'.
        """
        test_cases = []
        
        # Generate valid cases
        for _ in range(count):
            case = {"_is_valid": True}
            for param, cfg in cfgs.items():
                case[param] = self._generate_from_cfg(cfg)
            test_cases.append(case)
            
        # Generate invalid cases if provided
        if invalid_cfgs:
            # Strategy: For each parameter, generate a case where THAT parameter is invalid,
            # and others are valid (or invalid, but let's stick to one invalid param for clarity)
            # Actually, to ensure failure, at least one param must be invalid.
            
            for param, invalid_cfg in invalid_cfgs.items():
                # Generate a few cases where 'param' is invalid
                for _ in range(2): # Generate 2 invalid cases per parameter
                    case = {"_is_valid": False}
                    # Set the invalid parameter
                    case[param] = self._generate_from_cfg(invalid_cfg)
                    
                    # Set other parameters to valid values
                    for other_param, valid_cfg in cfgs.items():
                        if other_param != param:
                            case[other_param] = self._generate_from_cfg(valid_cfg)
                    
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
