a = int(input('digite um valor numerico: '))
if (a < 10):
    #se for digitado um numero menor que 10 trigga o bloco de função IF
    print('vc digitou um numero menor que 10')
elif (a < 100):
    #vai ser triggado se o anterior for falso e esse verdade
    print('vc digitou um numero menor que 100')
elif (a < 1000):
    #se for um numero maior que 1000
    print('vc digitou um numero menor que 1000')
else:
    print('vc digitou um numero maior ou igual a 1000')
    #se for maior que as anteriores
print('fim do programa')