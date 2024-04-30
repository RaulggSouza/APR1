#Faça um programa que receba um número N fornecido pelo usuário e mostre os N termos da série a seguir. 
#Depois, imprima a soma total da série.
n = int(input("Digite um número: "))
m = 1
soma = 0
for i in range(n):
    i += 1
    soma += i/m
    if i != n:
        print(f'{i}/{m}', end=" + ")
    else:
        print(f'{i}/{m}', end=" ")
    m += 2
print(f'= {soma:.2f}')