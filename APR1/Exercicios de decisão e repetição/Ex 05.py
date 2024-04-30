#5. Escreva um programa que leia um número n (número de termos de uma progressão aritmética), 
#a1 (o primeiro termo da progressão) e r (a razão da progressão) e apresenta os n termos desta progressão, 
#bem como a soma de todos elementos. 
n = int(input("Escreva o número de termos da progressão aritmética: "))
a = int(input("Escreva o primeiro termo da progressão: "))
r = int(input("Escreva a razão da progressão: "))
soma = 0
for i in range(n):
    if i == 0:
        print(a, end=" ")
        soma += a
    else: 
        a += r
        print(a, end=" ")
        soma += a
print(f'A soma dessa progressão aritmética é {soma}')
