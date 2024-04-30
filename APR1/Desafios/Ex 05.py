#5. Faça um programa que preencha uma matriz 7 x 7 de inteiros e crie duas listas com 7 posições cada que contenham, respectivamente, o maior elemento de cada linha e o menor elemento de cada linha. 
matriz = []
listaMaior = []
listaMenor = []
for i in range(7): #Linha
    linha = []
    for j in range(7): #Coluna
        num = int(input(f'Digite o número da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(num)
    matriz.append(linha)
for i in range(len(matriz)):
    maior = matriz[i][0]
    menor = matriz[i][0]
    for j in range(len(matriz[i])):
        if menor > matriz[i][j]:
            menor = matriz[i][j]
        if maior < matriz[i][j]:
            maior = matriz[i][j]
    listaMenor.append(menor)
    listaMaior.append(maior)
print("Lista dos números maiores: ", end="")
for i in range(len(listaMaior)):
    print(listaMaior[i], end=", ")
    if i == len(listaMaior)-1:
        print(listaMaior[i], end=".\n")
print("Lista dos números menores: ", end="")
for i in range(len(listaMenor)):
    print(listaMenor[i], end=", ")
    if i == len(listaMenor)-1:
        print(listaMenor[i], end=".")