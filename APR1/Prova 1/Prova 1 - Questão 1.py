#Faça um programa que preencha duas listas de A e B de tamanho N com valores inteiros. Em seguida,
#o programa deverá precorrer as listas criando uma lista C que representa a intersecção entre A e B.
# Ou seja, C conterá apenas os elementos que aparecem simultaneamente em A e B.
#Obs: Não usar operador in

a = []
b = []
c = []
auxiliar = [] #pega os valores iguais
n = int(input("Digite o tamanho das listas: "))
for i in range(n):
    num = int(input(f"Digite o {i+1}° elemento da lista A: "))
    a.append(num)
for i in range(n):
    num = int(input(f"Digite o {i+1}° elemento da lista B: "))
    b.append(num)
    
#Pega os valores de ambas as listas
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            auxiliar.append(a[i])

#Testa valores iguais
j = 0
comeco = 0
for i in range(len(auxiliar)):
    cont = 0
    comeco += 1 #Define o começo da contagem da lista, para que não se teste o mesmo termo
    j = comeco
    while j < len(auxiliar):
        if auxiliar[i] == auxiliar[j]:
            cont += 1
        j+=1
    if cont == 0:
        c.append(auxiliar[i])
c.sort()
#Imprime as listas
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
if len(c) != 0:
    print("Lista C: ", end="")
    for i in range(len(c)):
        if i+1 == len(c):
            print(c[i], end=".\n")
        else:
            print(c[i], end=", ")
else:
    print("Não existem valores que aparecem simultaneamente na lista A e B")