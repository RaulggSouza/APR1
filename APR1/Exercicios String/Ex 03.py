#3. Escreva um programa que verifique se duas strings fornecidas pelo usuário são iguais e mostre o total de caracteres de cada uma delas.Diferencie letras maiúsculas das minúsculas.
p1 = input("Digite a primeira palavra: ")
p2 = input("Digite a segunda palavra: ")
if p1 == p2:
    print("As palavras são iguais")
else:
    print("As palavras são diferentes")
print(f"Tamanho da primeira palavra: {len(p1)}")
print(f"Tamanho da segunda palavra: {len(p2)}")