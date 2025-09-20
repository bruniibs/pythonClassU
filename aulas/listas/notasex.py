# soma = 0
# cont = 0
# while cont<10:
#     nota = int(input(f"digite a {cont+1}a nota: ")) #digitando nota
#     soma += nota
#     cont += 1

# media = soma/10 #temos a media
# print(f"A media é {media}")

# soma = 0
# cont = 0
# qtd = int(input("Digite a quantidade de notas: "))
# while cont<qtd:
#     nota = int(input(f"digite a {cont+1}a nota: ")) #digitando nota
#     soma += nota
#     cont += 1

# media = soma/10 #temos a media
# print(f"A media é {media}")

soma = 0
cont = 's'
qtd = 0

while cont == 's':
    nota = int(input(f"Digite a {qtd+1}a nota: "))
    soma += nota
    qtd += 1
    cont = input("Deseja digitar mais notas s/n? ")
media = soma/qtd
print(f"A média é {media}")