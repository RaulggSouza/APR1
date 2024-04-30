#7. Faça um programa que calcule e apresente o mdc entre dois números. TERMINAR
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
divisor = 2
mdc = 1
while divisor<n1 or divisor<n2:
    if n1%divisor == 0 and n2%divisor == 0:
        mdc = divisor
    divisor += 1
print(f'O mdc de {n1} e {n2} é {mdc}')