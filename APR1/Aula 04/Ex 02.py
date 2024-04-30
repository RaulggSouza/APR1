#2. Crie um programa que leia inicialmente uma sequência de N notas de alunos fornecidas pelo usuário e ao final mostre a sequência 
#e sua média aritmética. Defina um critério de parada para a entrada denotas pelo usuário.
notas = []
continuar = True
soma = 0
contador = 0
i = 0
while continuar:
    num = float(input("Digite a nota do aluno, se não quiser mais inserir notas digite um valor negativo: "))
    if num >= 0:
        notas.append(num)
        contador += 1
    else:
        continuar = False
print("As notas do aluno são:", end=" ")
while i < contador:
    if i == contador-1:
        print(notas[i], end=" ")
    else:
        print(notas[i], end=", ")
    soma += notas[i]
    i+=1
print(f'e a média dele é {(soma/contador):.2f}')
