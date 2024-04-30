#Na teoria dos sistemas, o elemento MinMas de uma matriz é o maior elemento da linha onde se encontra o menor elemento
#da matriz. Faça um programa que preencha uma matriz de ordem NxM, percorra a matriz e imprima o seu MinMas e a
#posição (lina e coluna) que ele ocupa na matriz.
matriz = []
n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))
for i in range(n):
    linha = []
    for j in range(m):
        num = int(input(f"Digite o valor da {i+1}ª linha e {j+1}ª coluna: "))
        linha.append(num)
    matriz.append(linha)
menor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if menor > matriz[i][j]:
            menor = matriz[i][j]
            linhaMenor = i
colunaMaior = 0
maior = matriz[linhaMenor][0]
for i in range(len(matriz[linhaMenor])):
    if maior < matriz[linhaMenor][i]:
        maior = matriz[linhaMenor][i]
        colunaMaior = i
print(f"O MinMax da Matriz é {maior}, que está localizado na linha {linhaMenor} coluna {colunaMaior}")