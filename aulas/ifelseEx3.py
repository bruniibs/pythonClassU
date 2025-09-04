# n1 = int(input('insira um numero: '))
# n2 = int(input('insira outro numero: '))
# n3 = int(input('insira um numero: '))

# if(n1 > n2 and n1 > n3): #viu qye n1 é maior que todos
#     maior = n1 #gravou que n1 é o maior que todos
# elif(n2 > n3): #se chegou aqui é pq o n1 não é maior que o n2
#     maior = n2 #se for maior que o n3 vai salvar aqui
# else:
#     maior = n3

# print(maior)

n1 = int(input('insira um numero: '))
n2 = int(input('insira outro numero: '))
n3 = int(input('insira um numero: '))
maior = n1 #salvou falando que o n1 é o maior, ainda nao temos como comparar

#começamos a comparar agora
if n2>maior:
    maior = n2 #se o n2 for maior que o maior(n1 atualmente) ele atualiza a var maior com o n2
if n3>maior:
    maior = n3