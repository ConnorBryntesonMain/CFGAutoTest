import random
from typing import Dict, Any, List, Union

class CFG:
    def __init__(self, start_symbol: str, productions: Dict[str, List[str]]):
        self.start_symbol = start_symbol
        self.productions = productions

    def __repr__(self):
        return f"CFG(start={self.start_symbol}, productions={self.productions})"

class CFGGenerator:
    """
    Generates a Context Free Grammar based on function parameter bounds.
    """
    
    def from_bounds(self, bounds: Dict[str, Any]) -> Dict[str, CFG]:
        """
        Creates a CFG for each parameter in the bounds dictionary.
        
        Args:
            bounds: A dictionary mapping parameter names to their constraints.
            
        Returns:
            A dictionary mapping parameter names to their corresponding CFG.
        """
        cfgs = {}
        for param, constraints in bounds.items():
            cfgs[param] = self._create_cfg_for_param(param, constraints)
        return cfgs

    def _create_cfg_for_param(self, param: str, constraints: Dict[str, Any]) -> CFG:
        param_type = constraints.get("type", "unknown")
        
        if param_type == "int":
            return self._create_int_cfg(param, constraints)
        elif param_type == "str":
            return self._create_str_cfg(param, constraints)
        elif param_type == "float":
            return self._create_float_cfg(param, constraints)
        elif param_type == "bool":
            return self._create_bool_cfg(param)
        else:
            # Fallback for unknown types
            return CFG(start_symbol="S", productions={"S": ["<unknown>"]})

    def _create_int_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        # Simplified integer generation: S -> number
        # In a real CFG for integers, we might have S -> -D | D, D -> dD | d, etc.
        # Here we will generate a set of representative integers as productions
        min_val = constraints.get("min", -100)
        max_val = constraints.get("max", 100)
        
        # Generate a few sample values within range
        samples = set()
        samples.add(str(min_val))
        samples.add(str(max_val))
        samples.add(str((min_val + max_val) // 2))
        for _ in range(5):
             samples.add(str(random.randint(min_val, max_val)))
             
        productions = {"S": list(samples)}
        return CFG(start_symbol="S", productions=productions)

    def _create_float_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        min_val = constraints.get("min", -100.0)
        max_val = constraints.get("max", 100.0)
        
        samples = set()
        samples.add(str(min_val))
        samples.add(str(max_val))
        for _ in range(5):
             samples.add(str(random.uniform(min_val, max_val)))
             
        productions = {"S": list(samples)}
        return CFG(start_symbol="S", productions=productions)

    def _create_str_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        # S -> "string"
        max_len = constraints.get("max_length", 10)
        charset = constraints.get("charset", "alphanumeric")
        
        chars = []
        if charset == "alphanumeric":
            chars = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)] # a-z, 0-9
        
        # Generate sample strings
        samples = []
        for _ in range(5):
            length = random.randint(1, max_len)
            s = "".join(random.choice(chars) for _ in range(length))
            samples.append(f'"{s}"')
            
        productions = {"S": samples}
        return CFG(start_symbol="S", productions=productions)

    def _create_bool_cfg(self, param: str) -> CFG:
        return CFG(start_symbol="S", productions={"S": ["True", "False"]})
