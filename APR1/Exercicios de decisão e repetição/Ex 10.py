#10. Calcular e escrever o valor do número pi, com precisão de 0.0001, usando a série
#pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 TERMINAR
pi = 0
contador = 0
denominador = 1
while len(str(pi)) != 6:
    if contador%2 == 0:
        pi += 4/denominador
    else:
        pi -= 4/denominador
    contador += 1
    denominador += 2
print(pi)