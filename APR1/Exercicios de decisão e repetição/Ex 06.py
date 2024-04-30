#6. Faça um programa que calcule e apresente o mmc entre dois números.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
cont = True
mmc = n2
while cont:
    if mmc%n1 == 0 and mmc%n2 == 0:
        cont = False
        print(f'O mmc de {n1} e {n2} é {mmc}')
    else:
        mmc += 1