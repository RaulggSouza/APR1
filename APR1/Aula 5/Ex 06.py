#6. Escreva um programa que preencha uma matriz A m x n e uma matriz B n x p, ambas com valores inteiros. Em seguida, o programa deve mostrar a matriz A (mxn), a matriz B (nxp) e a matriz C (mxp),representando o produto entre A e B.
#Obs: A matriz C tem as dimensões m x p, ou seja, o número de linhas da primeira matriz e o número de colunas da segunda.
#TERMINAR
n = int(input("Digite um número inteiro: ")) #2
m = int(input("Digite outro número inteiro: ")) #3
p = int(input("Digite mais um número inteiro: ")) #3
a = []
b = []
c = []
def escreveMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
for i in range(m): #Linhas
    linha = []
    for j in range(n): #Colunas
        num = int(input(f"Digite o número da {i+1}° linha e {j+1}° coluna da Matriz A: "))
        linha.append(num)
    a.append(linha)
for i in range(n): #Linhas
    linha = []
    for j in range(p): #Colunas
        num = int(input(f"Digite o número da {i+1}° linha e {j+1}° coluna da Matriz B: "))
        linha.append(num)
    b.append(linha)
print(a)
print(b)
for i in range(m):
    linha = []
    for j in range(n):
        for k in range(p):
            if j == 0: #testa se ele está na primeira coluna
                linha.append(a[i][j]*b[j][k])
            else:
                linha[k] += a[i][j]*b[j][k]

    c.append(linha)
print("Matriz A:")
escreveMatriz(a)
print("Matriz B:")
escreveMatriz(b)
print("Matriz C:")
escreveMatriz(c)