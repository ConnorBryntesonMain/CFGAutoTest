import random
from typing import Dict, Any, List, Union

class CFG:
    def __init__(self, start_symbol: str, productions: Dict[str, List[str]], reasoning: str = ""):
        self.start_symbol = start_symbol
        self.productions = productions
        self.reasoning = reasoning

    def __repr__(self):
        return f"CFG(start={self.start_symbol}, productions={self.productions}, reasoning='{self.reasoning}')"

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
            return CFG(start_symbol="S", productions={"S": ["<unknown>"]}, reasoning="Unknown type, using placeholder")

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
        reasoning = f"Integer type. Range: [{min_val}, {max_val}]. Samples generated uniformly."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

    def _create_float_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        min_val = constraints.get("min", -100.0)
        max_val = constraints.get("max", 100.0)
        
        samples = set()
        samples.add(str(min_val))
        samples.add(str(max_val))
        for _ in range(5):
             samples.add(str(random.uniform(min_val, max_val)))
             
        productions = {"S": list(samples)}
        reasoning = f"Float type. Range: [{min_val}, {max_val}]. Samples generated uniformly."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

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
        reasoning = f"String type. Max Length: {max_len}. Charset: {charset}. Samples generated randomly."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

    def _create_bool_cfg(self, param: str) -> CFG:
        return CFG(start_symbol="S", productions={"S": ["True", "False"]}, reasoning="Boolean type. Values: True, False.")

    def create_invalid_cfg(self, bounds: Dict[str, Any]) -> Dict[str, CFG]:
        """
        Creates a CFG for generating invalid inputs (out of bounds, etc.) for each parameter.
        """
        cfgs = {}
        for param, constraints in bounds.items():
            cfgs[param] = self._create_invalid_cfg_for_param(param, constraints)
        return cfgs

    def _create_invalid_cfg_for_param(self, param: str, constraints: Dict[str, Any]) -> CFG:
        param_type = constraints.get("type", "unknown")
        
        if param_type == "int":
            return self._create_invalid_int_cfg(param, constraints)
        elif param_type == "float":
            return self._create_invalid_float_cfg(param, constraints)
        elif param_type == "str":
            return self._create_invalid_str_cfg(param, constraints)
        # Bool has no "invalid" values in type system usually, unless we pass non-bools, 
        # but here we stick to type-safe invalid values if possible (e.g. none for bool)
        # or just return valid ones if no invalid exists.
        return CFG(start_symbol="S", productions={"S": ["None"]}, reasoning="Invalid input: None")

    def _create_invalid_int_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        min_val = constraints.get("min", -100)
        max_val = constraints.get("max", 100)
        
        samples = set()
        # Generate values just outside the range
        samples.add(str(min_val - 1))
        samples.add(str(max_val + 1))
        samples.add(str(min_val - 100))
        samples.add(str(max_val + 100))
             
        productions = {"S": list(samples)}
        reasoning = f"Invalid Integer. Outside range [{min_val}, {max_val}]."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

    def _create_invalid_float_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        min_val = constraints.get("min", -100.0)
        max_val = constraints.get("max", 100.0)
        
        samples = set()
        samples.add(str(min_val - 0.1))
        samples.add(str(max_val + 0.1))
        samples.add(str(min_val - 100.0))
        samples.add(str(max_val + 100.0))
             
        productions = {"S": list(samples)}
        reasoning = f"Invalid Float. Outside range [{min_val}, {max_val}]."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

    def _create_invalid_str_cfg(self, param: str, constraints: Dict[str, Any]) -> CFG:
        max_len = constraints.get("max_length", 10)
        
        samples = []
        # Generate string longer than max_length
        long_str = "a" * (max_len + 1)
        samples.append(f'"{long_str}"')
        long_str_2 = "b" * (max_len + 10)
        samples.append(f'"{long_str_2}"')
            
        productions = {"S": samples}
        reasoning = f"Invalid String. Length > {max_len}."
        return CFG(start_symbol="S", productions=productions, reasoning=reasoning)

