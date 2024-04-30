#Escreva um programa que leia três números inteiros e os imprima em ordem crescente.
#Jeito 1
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
n3 = int(input("Digite o terceiro número "))

if n1 > n2:
    if n1>n3:
        maior = n1
        if n2>n3:
            meio = n2
            menor = n3
        else:
            meio = n3
            menor = n2
    else:
        maior = n3
        meio = n1
        menor = n2
elif n2 > n1:
    if n2>n3:
        maior = n2
        if n1>n3:
            meio = n1
            menor = n3
        else:
            meio = n3
            menor = n1
    else:
        maior = n3
        meio = n2
        menor = n1
elif n3 > n1:
    if n3>n2:
        maior = n3
        if n1>n2:
            meio = n1
            menor = n2
        else:
            meio = n2
            menor = n1
    else:
        maior = n2
        meio = n3
        menor = n1
print(f'{menor}, {meio}, {maior}')
#Jeito 2
lista = []
for i in range(3):
    n = int(input(f'Digite o {i+1}° número '))
    lista.append(n)
lista.sort()
print(lista)