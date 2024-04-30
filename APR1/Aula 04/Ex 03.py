#3. Crie um programa que leia inicialmente uma sequência de N números inteiros e ao seu final mostre a sequência
#original, a soma de seus elementos que forem pares e a multiplicação dos elementos que forem ímpares.
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
i = 0
soma = 0
vezes = 1
numeros = []
while i < quantidade:
    x = int(input(f"Digite o {i+1}° número: "))
    numeros.append(x)
    i += 1
print("Sequência inserida:", end=" ")
for i in range(len(numeros)):
    if numeros[i]%2 == 0:
        soma += numeros[i]
    else:
        vezes *= numeros[i]
    if i == len(numeros)-1:
        print(numeros[i], end=". ")
    else:
        print(numeros[i], end=", ")
print(f"Soma dos pares {soma} e mulitiplicação dos impares {vezes}")