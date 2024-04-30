#2. Faça um programa que imprima os 20 primeiros números primos.
contador = 1
num = 2
print("Os 20 primeiros números primos são: ")
while contador <= 20:
    primo = 0
    for i in range(num):
        if num%(i+1) == 0:
            primo += 1
    if primo == 2:
        print(num, end=" ")
        contador += 1
    num += 1