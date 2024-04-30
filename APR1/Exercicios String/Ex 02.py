#2. Escreva um programa que remove todas as ocorrências de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.
frase = input("Digite uma frase: ")
caracter = input("Digite o caractér a ser encontrado: ")
nova_frase = ""

for i in range(len(frase)):
    if frase[i] != caracter:
        nova_frase += frase[i]
        
print(nova_frase)
#print(frase.replace(caracter,""))