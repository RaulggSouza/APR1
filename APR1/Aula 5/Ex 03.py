#3. Faça um programa que solicite do usuário um valor N, representando adimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente,deverá criar a matriz transposta de A (A^t). Ao final, deve ser mostrada a matriz original e sua respectiva transposta. Lembre-se que a matriztransposta At será obtida a partir da matriz A trocando-se ordenadamente as linhas por colunas (ou as colunas por linhas), conforme o exemplo a seguir:
n = int(input("Digite a dimensão da matriz quadrada: "))
matriz = []
transposta = []
for i in range(n):
    linha = []
    for j in range(n):
        num = int(input(f"Digite o valor da {i+1}° linha e {j+1}° coluna: "))
        linha.append(num)
    matriz.append(linha)
print("Matriz original: ")
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
        linha.append(matriz[j][i])
    transposta.append(linha)
    print()
print("Matriz transposta: ")
for i in range(len(transposta)):
    for j in range(len(transposta[i])):
        print(transposta[i][j], end=" ")
    print()