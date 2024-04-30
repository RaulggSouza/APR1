#Faça um programa que mostre os 8 primeiros termos dasequência de Fibonacci. 
#Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55...
contador = 0
antecessor = 0
f = 1
x = 0
print(antecessor)
print(f)
while contador < 6:
    x = f
    f += antecessor
    antecessor = x
    contador += 1
    print(f)