#7. Faça um programa que permita ao usuário digitar o seu nome e em seguida o mostre de trás para frente utilizando somente letras maiúsculas.
nome = input("Digite seu nome: ")
contrario = ""
i = -1
for j in range(len(nome)):
    contrario += nome[i]
    i -= 1
print(contrario.upper())