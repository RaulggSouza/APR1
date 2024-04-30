#6. Crie um programa que dada uma sequência de N elementos fornecidos pelo usuário mostre a sequência original e a 
#sequência elevada ao cubo.
def imprimir(lista, expo=1):
    for i in range(len(lista)):
        if i == len(lista)-1:
            print((lista[i]**expo), end=". ")
        else:
            print(lista[i]**expo, end=", ")
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
numeros = []
for i in range(quantidade):
    x = int(input(f"Digite o {i+1}° número da primeira lista: "))
    numeros.append(x)
print("Sequência: ", end="")
imprimir(numeros)
print("Sequência ao cubo: ", end="")
imprimir(numeros,3)