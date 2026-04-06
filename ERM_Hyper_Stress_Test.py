import math

def erm_hyper_sieve(value, benchmark=1000):
    """
    NEDELCHEV HYPER-SIEVE: Stress Testing the Hybrid ERM.
    Validates mathematical constants against the Logic Fuse (???).
    """
    # 1. THE LOGIC FUSE (Hyper-Position Check)
    if not math.isfinite(value) or abs(value) > benchmark:
        return "???"  # The 'I don't know' / Singularity state
    
    # 2. THE TERNARY CORE (Balance Check)
    # Reducing the value to its discrete energy state
    core_state = int(round(value)) % 3
    
    # 3. THE BINARY MAPPING (Structural Anchor)
    mapping = {
        0: "00 (Absolute Balance)",
        1: "01 (Active Action)",
        2: "10 (Active Potential)"
    }
    
    return mapping.get(core_state, "11 (Structural Noise)")

# --- ПЪЛЕН ХИПЕР ТЕСТ (THE ABSOLUTE TEST) ---
phi = (1 + 5**0.5) / 2  # Златното сечение
pi = math.pi            # Числото Пи

stress_test = {
    "Zero Point (Truth)": 0,
    "Golden Ratio (Phi)": phi,
    "Circle Constant (Pi)": pi,
    "Standard Limit": 1000,
    "Beyond Standard": 1001,
    "Infinity Paradox": float('inf'),
    "Mathematical Singularity": float('nan')
}

print(f"{'PHENOMENON':<25} | {'VALUE':<15} | {'ERM DECISION'}")
print("-" * 65)

for name, val in stress_test.items():
    decision = erm_hyper_sieve(val)
    print(f"{name:<25} | {str(round(val, 4)) if math.isfinite(val) else str(val):<15} | {decision}")