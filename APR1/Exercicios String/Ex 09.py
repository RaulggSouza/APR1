#9. Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é umanagrama para “America”. Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco.O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.
contador = 0
f1 = input("Digite uma palavra ou frase: ")
f2 = input("Digite outra palavra ou frase: ")
f1, f2 = f1.upper(), f2.upper()
f1, f2 = f1.replace(" ", ""), f2.replace(" ","")
if len(f1) == len(f2):
    for i in range(len(f1)):
        cont1, cont2 = 0, 0 
        for j in range(len(f1)):
            if f1[i] == f1[j]:
                cont1 += 1
            if f1[i] == f2[j]:
                cont2 += 1
        if cont1 == cont2:
            contador += 1
    if contador == len(f1):
        resposta = f'{f2} é anagrama de {f1}'
    else:
        resposta = "Não são anagramas"
else: 
    resposta = "Não são anagramas"
print(resposta)