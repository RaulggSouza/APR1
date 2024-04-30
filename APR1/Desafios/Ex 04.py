#4. Na teoria dos sistemas, o elemento MINMAX de uma matriz é o maior elemento da linha em que se encontra o menor elemento da matriz. Elabore um programa que carregue uma matriz 4 x 5 com números reais, identifique e mostre o MINMAX e a sua posição na matriz. 
matriz = []
for i in range(4): #Linha
    linha = []
    for j in range(5): #Coluna
        num = int(input(f'Digite o número da {i+1}ª linha e {j+1}ª coluna: '))
        linha.append(num)
    matriz.append(linha)
menor = matriz[0][0]
linhaEscolhida = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if menor > matriz[i][j]:
            menor = matriz[i][j]
            linhaEscolhida = i
maior = matriz[linhaEscolhida][0]
for i in range(len(matriz[linhaEscolhida])):
    if maior < matriz[linhaEscolhida][i]:
        maior = matriz[linhaEscolhida][i]
        colunaMaior = i
print(f'O MINMAX da matriz é {maior} e ele está na posição {linhaEscolhida}x{colunaMaior}')