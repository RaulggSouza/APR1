#6. Faça um programa que solicite o nome do usuário e imprima-o navertical e em formato de escada.
nome = input("Digite seu nome: ")
palavra = ""
for letra in nome:
    palavra += letra
    print(palavra)