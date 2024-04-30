#Faça um programa que leia um número inteiro >= 0 e calcule o seu fatorial.
continuar = False
while continuar == False:
    num = int(input("Digite um número maior ou igual a 0: "))
    if num >= 0:
        continuar = True
    else:
        continuar = False
fatorial = 1
x = num
while continuar:
    if num == 0:
        continuar = False
    else:
        fatorial *= num
        num -= 1
print(f'O fatorial de {x} é {fatorial}')