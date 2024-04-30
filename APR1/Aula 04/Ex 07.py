#7. Crie um programa que leia inicialmente uma sequência de N números inteiros fornecidos pelo usuário e 
#mostre ao final da leitura a sequência original e a sequência invertida.
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
numeros = []
numeros_invertidos = []
for i in range(quantidade):
    x = int(input(f"Digite o {i+1}° número da lista: "))
    numeros.append(x)
print("Sequência Original: ", end="")
for i in range(len(numeros)):
    print(numeros[i], end=" ")
print("\nSequência Invertida: ", end="")
for i in range(len(numeros)):
    print(numeros[-(i+1)], end=" ")
