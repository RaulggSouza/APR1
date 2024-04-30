#7- Escrever um programa que preencha 2 matrizes (a e b) de 3 linhas x 4 colunas com números aleatórios e não repetidos (entre 0 e 100). Em seguida, verifique a existência de números iguais nas duas matrizes, imprimindo-os. No exemplo a seguir apenas o número 4 aparece em ambas matrizes.
#Matriz 1
#2 4 17 8
#5 10 3 19
#12 13 6 0
#Matriz 2
#12 14 27 18
#75 4 53 11
#52 93 61 30 
a = []
b = []
print("Digite apenas números entre 0 e 100 e não repita números dentro de uma mesma matriz")
for i in range(3): #Linha
    linha = []
    for j in range(4): #Coluna
        num = int(input(f'Digite o número da {i+1}ª linha e {j+1}ª coluna da matriz A: '))
        linha.append(num)
    a.append(linha)
for i in range(3): #Linha
    linha = []
    for j in range(4): #Coluna
        num = int(input(f'Digite o número da {i+1}ª linha e {j+1}ª coluna da matriz B: '))
        linha.append(num)
    b.append(linha)
print("Os seguintes números são repetidos em ambas as listas: ")
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(b)):
            if a[i][j] in b[k]:
                print(a[i][j])