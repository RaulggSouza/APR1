#Modifique o programa do exercício 1 de modo que a lista C represente a união das listas A e B. Ou seja conterá
# a junção dos elementos de A e B.
#Obs: não use o operador in
#Faça um programa que preencha duas listas de A e B de tamanho N com valores inteiros. Em seguida,
#o programa deverá precorrer as listas criando uma lista C que representa a intersecção entre A e B.
# Ou seja, C conterá apenas os elementos que aparecem simultaneamente em A e B.
#Obs: Não usar operador in

a = []
b = []
c = []
n = int(input("Digite o tamanho das listas: "))
for i in range(n):
    num = int(input(f"Digite o {i+1}° elemento da lista A: "))
    a.append(num)
for i in range(n):
    num = int(input(f"Digite o {i+1}° elemento da lista B: "))
    b.append(num)
c = a[:]
for i in range(len(b)):
    cont = 0
    for j in range(len(c)):
        if b[i] == c[j]:
            cont += 1
    if cont == 0:
        c.append(b[i])
c.sort()
print("Lista A: ", end="")
for i in range(len(a)):
    if i+1 == len(a):
        print(a[i], end=".\n")
    else:
        print(a[i], end=", ")
print("Lista B: ", end="")
for i in range(len(b)):
    if i+1 == len(b):
        print(b[i], end=".\n")
    else:
        print(b[i], end=", ")
print("Lista C: ", end="")
for i in range(len(c)):
    if i+1 == len(c):
        print(c[i], end=".\n")
    else:
        print(c[i], end=", ")