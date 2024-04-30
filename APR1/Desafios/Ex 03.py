#3. Crie um programa que preencha uma matriz 3x3 de números inteiros e verifique
#se essa matriz forma um quadrado mágico. Um quadrado mágico é formado
#quando a soma dos elementos de cada linha é igual:
#- à soma dos elementos de cada coluna da matriz;
#- à soma dos elementos da diagonal principal;
#- à soma dos elementos da diagonal secundária;
#Por exemplo, veja um quadrado mágico de lado 3 cujas somas sempre são 15:
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o número da {i+1}ª linha e {j+1}ª coluna: "))
        linha.append(num)
    matriz.append(linha)
somaLinha = []
somaColuna = []
somaDp = 0
somaDs = 0
for i in range(len(matriz)):
    somaL = 0
    somaC = 0
    somaDp += matriz[i][i]
    somaDs += matriz[i][-(i+1)]
    for j in range(len(matriz[i])):
        somaL += matriz[i][j] 
        somaC += matriz[j][i]
    somaLinha.append(somaL)
    somaColuna.append(somaC)
contador = 0
for i in range(len(somaLinha)):
    for j in range(len(somaColuna)):
        if somaLinha[i] == somaColuna[j] and somaLinha[i] == somaDp and somaLinha[i] == somaDs:
            contador += 1
if contador == 9:
    print("Essa matriz é um quadrado mágico")
else: 
    print("Essa matriz não é um quadrado mágico")