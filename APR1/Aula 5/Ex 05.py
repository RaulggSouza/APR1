#5. Escreva um programa que leia inteiros positivos m e n e os elementos de uma matriz A de números inteiros de dimensão m x n e ao final mostra a quantidade de linhas e colunas que tem apenas zeros (linhas nulas e colunas nulas).
n = int(input("Digite a quantidade de linhas da Matriz: "))
m = int(input("Digite a quantidade de colunas da Matriz: "))
matriz = []
contadorLinha = 0
contadorColuna = 0
linhaNula = 0
colunaNula = 0
for i in range(n):
    linha = []
    for j in range(m):
        num = int(input(f"Digite o número da {i+1}° linha e {j+1}° coluna: "))
        linha.append(num)
    matriz.append(linha)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 0:
            contadorLinha += 1
            if contadorLinha == 3:
                linhaNula += 1
    contadorLinha = 0
for i in range(m):
    for j in range(n):
        if matriz[j][i] == 0:
                contadorColuna += 1
                if contadorColuna == 3:
                    colunaNula += 1
    contadorColuna = 0
print(matriz)
print(f'Quantidade de linhas nulas: {linhaNula} e quantidade de colunas nulas: {colunaNula}')