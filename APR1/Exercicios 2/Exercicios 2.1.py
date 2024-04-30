#Faça um programa que receba 5 números inteiros e informe o maior entre eles.

#Jeito 1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    maior = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
else:
    maior = n5
print(f'O maior número é o {maior}')
#Jeito 2
lista = []
for i in range(5):
    n = int(input(f'Digite o {i+1}° número '))
    lista.append(n)
print(f'O maior número é o {max(lista)}')