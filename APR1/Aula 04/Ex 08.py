#8. Crie um programa que leia inicialmente uma sequência de N elementos inteiros positivos fornecidos pelo usuário 
#e substitua seus elementos de valor ímpar por -1 e os pares por +1. 
#Ao final imprima a sequência original e a sequência alterada
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
numeros = []
numeros_invertidos = []
continuar = False
x = -1
for i in range(quantidade):
    x = int(input(f"Digite o {i+1}° número positivo da lista: "))
    numeros.append(x)
print("Sequência Original: ", end="")
for i in range(len(numeros)):
    print(numeros[i], end=" ")
print("\nSequência Alterada: ", end="")
for i in range(len(numeros)):
    if numeros[i]%2 == 0:
        print("+1", end=" ")
    else:
        print("-1", end=" ")