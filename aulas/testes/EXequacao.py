import math

print("=" * 50)
print("RESOLUCAO DE EQUACAO DE SEGUNDO GRAU")
print("Formato: ax² + bx + c = 0")
print("=" * 50)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(f"\nEquação: {a}x² + {b}x + {c} = 0")

# verificacao se eh uma equacao de 2nd grau
if a == 0:
    print("Não é uma equação de segundo grau (a=0)")
else:
    delta = b**2 - 4*a*c
    print(f"Delta (V) = b² - 4ac = {delta}")
    
    if delta < 0:
        print("Delta negativo: Não existem raizes reais")
    elif delta == 0:
        raiz = b / (2*a)
        print(f"Delta zero: Raiz unica (x' = x'') = {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta) / (2*a))
        raiz2 = (-b + math.sqrt(delta) / (2*a))
        print(f"Delta positiva: duas raizes reais distintas")
        print(f"x' = {raiz1:.2f}")
        print(f"x'' = {raiz2:.2f}")

print("=" * 50)