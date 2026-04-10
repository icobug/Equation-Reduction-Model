# =============================================================================
# Equation Reduction Model (ERM) - Core Logic
# Author: Hristo Valentinov Nedelchev (2026)
# License: GNU General Public License v3.0 or later
# =============================================================================
# This script implements the Unified Theory of the Entropy Reduction Mechanism,
# translating continuous variables to a discrete state-space and establishing
# a universal filter for mathematical truth and structural integrity.
# =============================================================================

import math

class EquationReductionModel:
    def __init__(self):
        # The Theory of the "Smart Zero": Limiting division-by-zero crashes.
        # Defines the mathematical limit to prevent infinite loops and paradoxes.
        self.smart_zero = 1e-17
        
        # Binary Hybrid Logic Information States
        self.information_states = {
            "00": "Truth",
            "01": "Positive",
            "10": "Negative",
            "11": "Hyper-Position"
        }

    def calculate_f(self, a, b, c):
        """
        Core Mathematical Principle: Discrete Energy States
        Calculates the invariant function over a triple of variables.
        F(a,b,c) = a^2 + b^2 + c^2 - (ab + bc + ca)
        """
        return (a**2) + (b**2) + (c**2) - ((a * b) + (b * c) + (c * a))

    def evaluate_state(self, a, b, c):
        """
        Measures the logical distance from absolute equilibrium and classifies the state.
        Variables a, b, c are typically within {-1, 0, 1}.
        """
        f_value = self.calculate_f(a, b, c)
        
        if f_value > 0:
            # The structure possesses energy capacity and logical resilience.
            state = "Valid State (Truth)"
        elif f_value == 0:
            # A total absence of potential difference, leading to logical stagnation.
            state = "Invalid State (Entropy)"
        else:
            state = "Unknown State"
            
        return {"F_value": f_value, "Classification": state}

    def get_signal_state(self, binary_code):
        """
        Maps the binary/hybrid input to the ERM foundational information states.
        """
        return self.information_states.get(binary_code, "Unknown/Noise")

    def safe_divide(self, numerator, denominator):
        """
        Applies the 'Smart Zero' fuse to allow the system to navigate 
        through singularities without computational collapse.
        ERM_out = lim(e -> 10^-17) f(x + e)
        """
        if abs(denominator) < self.smart_zero:
            # Prevents systemic crash by substituting absolute zero with the Smart Zero limit
            adjusted_denominator = self.smart_zero if denominator >= 0 else -self.smart_zero
            return numerator / adjusted_denominator
        
        return numerator / denominator

    def process_equation(self, numerator, denominator, a, b, c):
        """
        Comprehensive stress-test function processing a single operation through 
        the discrete algebraic sieve and paradox resolution.
        """
        state_info = self.evaluate_state(a, b, c)
        resolution = self.safe_divide(numerator, denominator)
        
        return {
            "Energy_State": state_info,
            "Resolved_Output": resolution,
            "System_Status": "Stable (Paradox Avoided)" if abs(denominator) < self.smart_zero else "Stable"
        }

# =============================================================================
# Demonstration and Execution
# =============================================================================
if __name__ == "__main__":
    erm = EquationReductionModel()
    
    print("=== ERM (Equation Reduction Model) Initialized ===\n")
    
    # 1. Testing Core Energy States (Truth vs Entropy)
    print("--- 1. Discrete Energy States Analysis ---")
    valid_test = erm.evaluate_state(1, -1, 0)
    print(f"Test Input (1, -1, 0) -> F={valid_test['F_value']} | {valid_test['Classification']}")
    
    invalid_test = erm.evaluate_state(0, 0, 0)
    print(f"Test Input (0, 0, 0)  -> F={invalid_test['F_value']} | {invalid_test['Classification']}")
    
    # 2. Testing Smart Zero Paradox Resolution
    print("\n--- 2. Smart Zero Paradox Resolution ---")
    num, den = 10, 0
    print(f"Attempting standard division: {num} / {den}")
    try:
        erm_result = erm.safe_divide(num, den)
        print(f"[ERM Success]: Operation bypassed singularity. Output = {erm_result}")
    except Exception as e:
        print(f"[Standard AI Crash]: {e}")
        
    # 3. Testing Information States
    print("\n--- 3. Hybrid Information State Mapping ---")
    print(f"Code '00' -> {erm.get_signal_state('00')}")
    print(f"Code '11' -> {erm.get_signal_state('11')}")