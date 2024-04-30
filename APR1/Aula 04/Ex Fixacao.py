#1. Faça um programa que crie uma lista com 10 números inteiros fornecidos pelo usuário. Após criar a lista, o programa deverá imprimir:
# O maior elemento da lista
# O menor elemento da lista
# A soma de todos os elementos da lista
# Os elementos ímpares
# Os elementos maiores do que 18
#Obs: não use funções prontas.
numeros = []
tam = 10
for i in range(tam):
    num = int(input(f"Digite o {i+1}° número inteiro: "))
    numeros.append(num)

#Testa o maior
maior = numeros[0]
i = 0
while i < tam:
    if numeros[i] > maior:
        maior = numeros[i]
    i += 1
print(f'O maior número da lista é o {maior}')

#Testa o menor
menor = numeros[0]
i = 0
while i < tam:
    if menor > numeros[i]:
        menor = numeros[i]
    i += 1
print(f'O menor número da lista é o {menor}')

#Soma
soma = 0
i = 0
while i < tam:
    soma += numeros[i]
    i += 1

#Impares
i = 0
impares = []
while i < tam:
    if numeros[i]%2 != 0:
        impares.append(numeros[i])
    i += 1
if len(impares) == 0:
    print("A lista não possui números impares")
else:
    print(f'Os números impares da lista são: {impares}')

#Maiores que 18
i = 0
maiores = []
while i < tam:
    if numeros[i] > 18:
        maiores.append(numeros[i])
    i += 1
if len(maiores) == 0:
    print("A lista não possui números maiores que 18")
else:
    print(f'Os números maiores que 18 da lista são: {maiores}')
