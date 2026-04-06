import math

class HybridERM:
    """
    Hybrid Equation Reduction Model (ERM) Implementation.
    Developed by Hristo Valentinov Nedelchev.
    Bridges Ternary Logic (-1, 0, 1) with Binary Structural Mapping.
    """
    
    def __init__(self, benchmark=100):
        self.benchmark = benchmark  # The limit of the 'Standard'
        
    def core_reduction(self, value):
        """Phase 1: Ternary reduction of the energy state."""
        return int(value) % 3

    def binary_mapping(self, erm_state):
        """Phase 2: Mapping ERM to structural binary states."""
        mapping = {
            0: "00 (Absolute Balance)",
            1: "01 (Positive Potential)",
            2: "10 (Negative Potential)" # 2 is effectively -1 in mod 3
        }
        return mapping.get(erm_state, "11 (Error)")

    def process(self, value):
        """Phase 3: The Hybrid Intelligence Layer with Hyper-Position Guard."""
        
        # 1. Check for Paradoxes / Singularities (The Guard)
        if not math.isfinite(value) or abs(value) > self.benchmark:
            return "???" # Hyper-Position: Unknown / Beyond Benchmark
            
        # 2. Process through Core and Structure
        erm_state = self.core_reduction(value)
        structure = self.binary_mapping(erm_state)
        
        return structure

# --- ТЕСТОВ ПУЛС ---
erm_system = HybridERM(benchmark=1000)

test_cases = {
    "Pythagoras Result": 0,           # Perfect Balance
    "Active Signal": 1,               # Presence
    "Structural Error": 11,           # Deviation
    "Black Hole": float('inf'),       # Paradox
    "Beyond Standard": 9999           # Limit reached
}

print("--- HYBRID ERM LOGIC TEST ---")
for name, val in test_cases.items():
    result = erm_system.process(val)
    print(f"{name:20} | Input: {str(val):10} | Output: {result}")