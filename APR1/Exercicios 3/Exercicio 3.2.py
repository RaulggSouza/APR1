#Faça um programa que exiba todos os números de 1 a 100 que são divisíveis por 7 e por 3.
for i in range(100):
    if (i+1) % 7 == 0 and (i+1) % 3 == 0:
        print(i+1)