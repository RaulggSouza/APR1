#5. Faça um programa que recebe uma frase e retorna o número de palavras que a frase contém.
#frase = input("Digite uma frase: ")
#palavras = frase.split()
#print(f"A frase possui {len(palavras)} palavras")

#Fazer sem split
frase = input("Digite uma frase: ")
palavra = False
qntd_palavras = 0
for i in range(len(frase)):
    if frase[i] == " ":
        palavra = False
    else:
        palavra = True
    if (not palavra and frase[i-1] != " " and i > 0) or (i+1 == len(frase) and frase[i] !=" "):
        qntd_palavras += 1
print(f'Essa frase tem {qntd_palavras} palavras')