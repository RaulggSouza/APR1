#Faça um programa em Python que receba dois valores inteiros, representando a base e o expoente. 
#O programa deverá calcular eapresentar o resultado da base elevada ao expoente. 
#Por exemplo, para base = 5 e expoente = 3, ou seja, 5³, o programa deverá imprimir 125.
# Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de repetição.
base = int(input("Digite a base "))
expo = int(input("Digite o expoente "))
valor = 1
for i in range(expo):
    valor = valor*base
print(valor)
