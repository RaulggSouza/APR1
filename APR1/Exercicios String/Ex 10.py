#10. Escreva um programa que solicite ao usuário a entrada de um número inteiro positivo ou negativo e mostre a quantidade de dígitos desse número.
# numero = int(input("Digite um número inteiro positivo ou negativo: "))
# if numero >= 0:
#     print(f'Esse número tem {len(str(numero))} digitos')
# else:
#     print(f'Esse número tem {len(str(numero))-1} digitos')

num = input("Digite um número inteiro positivo ou negativo: ")
numeros = ['0','1','2','3','4','5','6','7','8','9']
contador = 0
neg = False
for i in range(len(num)):
    if i == 0 and num[0] == "-":
        neg = True
    for j in range(len(numeros)):
        if num[i] == numeros[j]:
            contador += 1
if contador == len(num)-1 and neg:
    print(f'Esse número tem {contador} digitos')
elif contador == len(num) and not neg:
    print(f'Esse número tem {len(num)} digitos')
else:
    print("Não é um número")       