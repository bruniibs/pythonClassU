maior = 0
num = int(input("Dgite um numero maior que 0: "))

while num>0:
    if num>maior:
        maior = num
    num = int(input("Digite outro numero maior que 0: "))

print(f"O maior valor digitado é {maior}")