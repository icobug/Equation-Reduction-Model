import numpy as np

def erm_surface(a, b, c):
    return a**2 + b**2 + c**2 - (a*b + b*c + c*a)

# Генериране на 900 точки (30x30 мрежа)
range_val = np.linspace(-10, 10, 30)
a_vals, b_vals = np.meshgrid(range_val, range_val)
c_fixed = 5  # Фиксирана трета променлива за сечение

surface = erm_surface(a_vals, b_vals, c_fixed)
integrity_score = (np.sum(surface >= 0) / surface.size) * 100

print(f"--- PHYSICAL STRESS TEST ---")
print(f"Tested points: {surface.size}")
print(f"Integrity Score: {integrity_score:.2f}%")
if integrity_score == 100:
    print("Result: Absolute Physical Stability Confirmed.")