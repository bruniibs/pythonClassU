nota = float(input('insira sua nota: '))

if (nota >= 60):
    print('vc foi aprovado')
elif(nota >= 40):
    #como ja foi verificado acima no IF que não é maior q 60 ele só vai até 59 nesse elif
    print('vc ficou de exame')
else:
    print('vc foi reprovado')
print('fim')