aux = 0
cont = 2
num = int(input("Digite um numero: "))

if num < 2:
    print(f"{num} não é primo")
else:
    while cont < num:
        if num % cont == 0:
            aux += 1
            break
        cont += 1
    if aux > 0:
        print(f"{num} não é primo")
    else:
        print(f"{num} é primo")