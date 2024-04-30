#Faça um programa que imprima os n primeiros termos da série de Fibonaci, onde n deve ser informado pelo
#usuário
n = int(input("Digite quantos termos aparecerão da sequência de Fibonaci: "))
antecessor = 0
numero = 1
auxiliar = 0
fib = [antecessor, numero]
for i in range(n-2):
    fib.append(antecessor+numero)
    auxiliar = numero
    numero += antecessor
    antecessor = auxiliar
print("Sequência de Fibonaci: ")
for i in range(len(fib)):
    if i+1 == len(fib):
        print(fib[i], end=".\n")
    else:
        print(fib[i], end=", ")