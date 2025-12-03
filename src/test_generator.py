import random
from typing import List, Any, Dict
from .cfg_generator import CFG

class TestGenerator:
    """
    Generates test inputs based on a Context Free Grammar.
    """
    
    def generate_test_case(self, cfg: CFG) -> str:
        """
        Generates a single test case string from the CFG.
        
        Args:
            cfg: The Context Free Grammar to use.
            
        Returns:
            A string generated from the start symbol.
        """
        return self._expand_symbol(cfg, cfg.start_symbol, depth=0)

    def _expand_symbol(self, cfg: CFG, symbol: str, depth: int) -> str:
        if depth > 1024: # Safety break for recursion
            return ""
            
        if symbol not in cfg.productions:
            return symbol
            
        production = random.choice(cfg.productions[symbol])
        
        # Parse production for non-terminals <Symbol>
        result = ""
        i = 0
        while i < len(production):
            if production[i] == '<':
                # Find end of tag
                end = production.find('>', i)
                if end != -1:
                    tag = production[i+1:end]
                    # Recursively expand. Note: We strip the brackets for the lookup key
                    result += self._expand_symbol(cfg, tag, depth + 1)
                    i = end + 1
                    continue
            result += production[i]
            i += 1
            
        return result
