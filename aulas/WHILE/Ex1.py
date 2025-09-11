print('Calculo fatorial')

# O programa funciona da seguinte forma:
# Lê um número do usuário
# Inicializa o fatorial como 1 e um contador com o valor do número
# Enquanto o contador for maior que 0, multiplica o fatorial pelo contador e decrementa o contador
# Exibe o resultado final
# Para 5! o cálculo seria: 5 × 4 × 3 × 2 × 1 = 120

# entrada dos dados
num = float(input('Insira um numero: '))

#inicialização das variaveis
fatorial = 1
contador = num

#calculo do fatorial usando while
while contador > 0: #diz que enquanto a var contador for 0
    fatorial *= contador #efetua o calculo (multiplica o fatorial pelo contador atual)
    contador -= 1 #tira uma unidade do contador

print(f'{num}! = {fatorial}')