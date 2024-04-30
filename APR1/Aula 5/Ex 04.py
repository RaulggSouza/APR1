#4. Faça um programa que crie uma matriz A de tamanho n x n de valores inteiros informados pelo usuário. O programa deverá verificar se A é uma matriz identidade e imprimir uma mensagem informando o usuário. Considere que a matriz identidade possui todos os elementos da diagonal principal iguais a 1 e os demais elementos iguais a 0, como no exemplo:
n = int(input("Digite a dimensão da matriz quadrada: "))
matriz = []
contadorPrincipal = 0
contadorResto = 0
for i in range(n):
    linha = []
    for j in range(n):
        num = int(input(f"Digite o valor da {i+1}° linha e {j+1}° coluna: "))
        linha.append(num)
    matriz.append(linha)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            contadorPrincipal += 1
        elif matriz[i][j] == 0:
            contadorResto += 1
if contadorPrincipal == n and contadorResto == n**2-n:
    print("É uma matriz identidade")
else:
    print("Não é uma matriz identidade")