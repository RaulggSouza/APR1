#1 Escreva um programa que remove a primeira ocorrência de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.
frase = input("Digite uma frase: ")
caracter = input("Digite o caractér a ser encontrado: ")
nova_frase = ""
contador = 0
for i in range(len(frase)):
    if frase[i] == caracter and contador == 0:
       contador += 1
    else:
        nova_frase += frase[i]

print(nova_frase)

#print(frase.replace(caracter,"",1))