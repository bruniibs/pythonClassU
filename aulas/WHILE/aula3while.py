#programa com break

soma = 0
qtd = 0
while True:
    n = float(input('Digite um numero: '))
    if n==0:
        break
    soma+=n
    qtd+=1
print(f'Quantidade = {qtd}')
print(f'Soma = {soma}')