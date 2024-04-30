#4. Crie um programa que leia inicialmente uma sequencia de N números inteiros. 
#Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira: uma sem repetição de elementos e 
#outra com os elementos que se repetem na lista original.
def imprimir(lista):
    for i in range(len(lista)):
        if i == len(lista)-1:
            print(lista[i], end=". ")
        else:
            print(lista[i], end=", ")
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
i = 0
numeros = []
repetidos = []
sem_repeticao = []
num = 0
while i < quantidade:
    x = int(input(f"Digite o {i+1}° número: "))
    numeros.append(x)
    i += 1
original = numeros[:]
for i in range(len(numeros)):
    num = numeros[i]
    numeros[i] = "a"
    if num in numeros:
        repetidos.append(num)
    elif num in repetidos:
        repetidos.append(num)
        sem_repeticao.append(num)
    else:
        sem_repeticao.append(num)
sem_repeticao.sort()
print("Lista original:", end=" ")
imprimir(original)
print("Lista com repetição:", end=" ")
imprimir(repetidos)
print("Lista sem repetição:", end=" ")
imprimir(sem_repeticao)
#print(f'Da lista original {original}, os números repetidos são {repetidos} e os não repetidos são {sem_repeticao}')