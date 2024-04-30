#5. Crie um programa que leia inicialmente duas sequências de N elementos cada uma e ao final mostre as duas 
#sequências originais e a sequência resultante da soma de seus elementos. Exemplo:
#a=[5, 9, 0] b=[12, 34, 101] soma=[17, 43, 101]
quantidade = int(input("Digite o números de termos que você deseja inserir na lista: "))
lista_a = []
lista_b = []
soma = []
num = 0
for i in range(quantidade):
    x = int(input(f"Digite o {i+1}° número da primeira lista: "))
    lista_a.append(x)
for i in range(quantidade):
    x = int(input(f'Digite o {i+1}° número da segunda lista: '))
    lista_b.append(x)
for i in range(quantidade):
    soma.append(lista_a[i] + lista_b[i])
print(f'Primeira lista {lista_a} + Segunda lista {lista_b} = {soma}')