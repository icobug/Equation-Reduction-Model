import sympy as sp

# Дефиниране на символи
a, b, c = sp.symbols('a b c', real=True)

# Уравнения за проверка
erm_eq = a**2 + b**2 + c**2 - (a*b + b*c + c*a)
pythagoras = a**2 + b**2 + c**2
linear_fail = a + b + c

def symbolic_proof(expr, name):
    # Проверка дали може да се представи като сума от квадрати (винаги >= 0)
    # За ERM това е 0.5 * ((a-b)**2 + (b-c)**2 + (c-a)**2)
    proof_form = 0.5 * ((a-b)**2 + (b-c)**2 + (c-a)**2)
    is_identical = sp.simplify(expr - proof_form) == 0
    
    print(f"Checking {name}...")
    if is_identical:
        print(f"💎 SUCCESS: {name} is a Fundamental Universal Invariant.")
    else:
        print(f"⚠️ NOTE: {name} is a standard or conditional structure.")

print("--- SYMBOLIC UNIVERSAL CHECKER ---")
symbolic_proof(erm_eq, "ERM Invariant")
print(f"Algebraic expansion of ERM: {sp.expand(erm_eq)}")