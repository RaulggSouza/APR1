#Faça um programa em Python que leia um conjunto de valores correspondentes às notas que os alunos obtiveram 
#em uma prova de Algoritmos. Quando o valor fornecido for um número
#negativo, significa que não existem mais notas para serem lidas. Após isso seu programa deverá:
# Escrever quantas notas são maiores ou iguais a 6.0
# Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
# Escrever quantos notas são menores que 4.0
# Escrever a média das notas fornecidas pelo usuário.
print("Insira as notas do aluno, se não houverem mais notas digitar um número negativo")
continuar = True
maior, meio, menor, média = 0, 0, 0, 0 
while continuar:
    nota = float(input("Digite a nota "))
    if nota > 0: 
        if nota >= 6.0:
            maior += 1
        elif nota >= 4.0 and nota < 6.0:
            meio += 1
        else:
            menor += 1
        média += nota
    else:
        continuar = False
print(f'Notas maiores que 6.0: {maior}')
print(f'Notas entre 4.0 e 6.0: {meio}')
print(f'Notas menores que 4.0: {menor}')
print(f'Média das notas: {média/(maior+meio+menor)}')
