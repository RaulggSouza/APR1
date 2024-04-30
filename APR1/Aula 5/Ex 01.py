#1. Crie um programa que solicita do usuário um valor N representando aquantidade linhas e um valor M representando a quantidade de colunas de uma matriz. Depois, o programa deverá solicitar do usuário N x M elementos para serem incluídos na matriz. Por fim, o programa deverá percorrer a matriz para encontrar e imprimir o seu maior elemento e o seu menor elemento.
n = int(input("Digite a quantidade de linhas da Matriz: "))
m = int(input("Digite a quantidade de colunas da Matriz: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        num = int(input(f"Digite o número da {i+1}° linha e {j+1}° coluna: "))
        linha.append(num)
    matriz.append(linha)
maior = matriz[0][0]
menor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if maior < matriz[i][j]:
            maior = matriz[i][j]
        if menor > matriz[i][j]:
            menor = matriz[i][j]
print(f'Maior número: {maior}, menor número: {menor}')