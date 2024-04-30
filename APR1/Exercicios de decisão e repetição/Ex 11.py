#Faça um programa que calcule e escreva a soma dos 20 primeiros termos da série: 
#100/0! + 99/1! ...
contador = 1
soma = 0
numerador = 100
num = 0
continuar = True
while contador < 20:
    fatorial = 1
    while continuar:
        if num == 0:
            continuar = False
        else:
            fatorial *= num
            num -= 1
    soma += numerador/fatorial
    num += 1
    numerador -= 1
    contador += 1
print(soma)