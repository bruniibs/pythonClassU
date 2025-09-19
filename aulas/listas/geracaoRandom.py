import random
lista1 = []
while (len(lista1)<10):
    num = random.randint(1,10)
    print(num) #mostrando valor que for gerado
    if not(num in lista1):#verdade se a var num nao estiver na lista
        lista1.append(num)

print(lista1)
lista1.sort()
print(lista1)