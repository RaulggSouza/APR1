#4. Escreva um programa que reconhece se uma string é um palíndromo.Exemplo: arara, ovo, reter.
palavra = input("Digite uma palavra: ")
palavra.upper()
palavra = palavra.replace(" ", "")
contador = 0
j = len(palavra)-1
for i in range(len(palavra)):
    if palavra[i] == palavra[j]:
        contador += 1
    j -= 1
if contador == len(palavra):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")