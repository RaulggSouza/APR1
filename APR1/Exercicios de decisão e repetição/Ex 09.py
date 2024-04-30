""" 9. Escreva um programa que apresente os 5 primeiros números perfeitos. Um
número perfeito é aquele que é igual a soma dos seus divisores (por exemplo, 6 =
1+2+3 e 28= 1+2+4+7+14). """
numeros_perfeitos = 0
numero = 2
divisor = 1
soma = 1
print("Os 5 primeiros números perfeitos são: ")
while numeros_perfeitos < 5:
    #num = numero
    divisor = numero//2
    while divisor > 1:
        if numero%divisor == 0:
            soma += divisor
            print(soma)
        divisor -=1
    if soma == numero:
        print(soma, end=" ")
        numeros_perfeitos += 1
    else:
        numero += 1
        soma = 1