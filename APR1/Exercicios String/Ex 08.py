#8. Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e aquantidade de vezes que aparecem as vogais a, e, i, o, u.
frase = input("Digite uma frase: ")
espacos, vogal = 0, 0
vogais = "aeiou"
for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra.lower() in vogais:
        vogal += 1
print(f'{espacos} = quantidade de espaços')
print(f'{vogal} = quantidade de vogais')