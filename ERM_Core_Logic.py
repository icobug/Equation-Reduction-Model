import numpy as np
import itertools

def calculate_entropy(values):
    unique, counts = np.unique(values, return_counts=True)
    probs = counts / len(values)
    return -np.sum(probs * np.log2(probs))

# 1. Генериране на пространството {-1, 0, 1}
states = [-1, 0, 1]
combos = list(itertools.product(states, repeat=3))

# 2. Основно ERM уравнение
def erm_function(a, b, c):
    return a**2 + b**2 + c**2 - (a*b + b*c + c*a)

results = [erm_function(*c) for c in combos]

# 3. Анализ на резултатите
valid_states = sum(1 for r in results if r >= 0)
efficiency = (calculate_entropy(results) / np.log2(len(np.unique(results)))) * 100

print(f"--- ERM CORE LOGIC ---")
print(f"Total combinations: {len(combos)}")
print(f"Stable states found: {valid_states}/{len(combos)}")
print(f"Information Efficiency: {efficiency:.2f}%")
print(f"Unique energy levels: {np.unique(results)}")