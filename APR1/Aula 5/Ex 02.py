#2. Faça um programa que solicite do usuário um valor N, representando a dimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente,deverá verificar se A é simétrica. A matriz será simétrica se e somente se todo elemento A[i,j] = A[j,i]. Segue um exemplo de matriz simétrica:
n = int(input("Digite a dimensão da matriz quadrada: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        num = int(input(f"Digite o valor da {i+1}° linha e {j+1}° coluna: "))
        linha.append(num)
    matriz.append(linha)
contador = 0
for i in range(len(matriz)):
    print(matriz[i])
    for j in range(len(matriz[i])):
        if matriz[i][j] == matriz[j][i]:
            contador += 1
if contador == n**2:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")