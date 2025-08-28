
horasT = float(input('quantas horas vc trabalhou: '))
valorH = int(input('qual o valor recebido por hora? '))
inss = int(input('qual a porcentagem de desconto do inss? '))

salBruto = valorH*horasT
liquido = salBruto-inss
desconto = salBruto-liquido

mensagem = f"voce recebe R$ {salBruto} de salario bruto, tem um desconto de R$ {desconto} e recebe R$ {liquido} de liquido"
print(mensagem)