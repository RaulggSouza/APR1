""" 8. Escreva um programa que leia um número não determinado de valores inteiros,
calcula e apresenta: a média aritmética dos valores lidos, a quantidade de valores
positivos, a quantidade de valores negativos e o percentual de valores negativos e
positivos. Obs: o programa deverá encerrar a leitura dos números, somente
quando o usuário desejar.  """
entrada = False
quantidade = 0
soma = 0
qPos = 0
qNeg = 0
while entrada == False:
    num = int(input("Digite um valor inteiro, (se não quiser inserir mais valores digite -9999): "))
    if num != -9999:
        quantidade += 1
        soma += num
        if num > 0:
            qPos += 1
        else:
            qNeg += 1
    else:
        entrada = True
taxaPos = qPos*100/quantidade
taxaNeg = qNeg*100/quantidade
print(f'''Soma: {soma}, Média: {soma/quantidade:.2f}, Quantidade de números positivos: {qPos}, Quantidade de números 
negativos: {qNeg}, Porcentual de positivos: {taxaPos:.2f}, Porcentual de negativos: {taxaNeg:.2f}''')