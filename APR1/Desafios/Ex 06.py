#6. Crie um programa que preencha uma matriz 10 x 20 de números inteiros e some cada uma das linhas, armazenando o resultado das somas em uma lista. Em seguida, o programa deverá multiplicar cada elemento da matriz pelo elemento da linha correspondente na lista e mostrar a matriz resultante.
matriz = []
for i in range(10): #Linha
    linha = []
    for j in range(20): #Coluna
        num = int(input(f'Digite o número da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(num)
    matriz.append(linha)
listaSomas = []
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
    listaSomas.append(soma)
print(listaSomas)
listaMulti = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j]*listaSomas[i])
    listaMulti.append(linha)
print(listaMulti)