#10. Faça uma função que receba 2 listas de valores inteiros e retorne a lista UNIÃO.

def Inteiro(n):
    contador = 0
    numeros = ['0','1','2','3','4','5','6','7','8','9','-']
    for i in range(len(n)):
        for j in range(len(numeros)):
            if n[i] == numeros[j]:
                contador += 1
    if contador == len(n):
        return True
    else: 
        return False

def popula_lista(lista):
    i = 0
    tam = int(input("Digite o tamanho da lista: "))
    while i < tam:
        num = input(f"Digite a {i+1}ª nota: ")
        if Inteiro(num):
            lista.append(float(num))
            i += 1
        else:
            print("Número não real, insira outro valor")

def uniao(a,b):
    uni = a[:]
    for i in range(len(b)):
        if b[i] not in a:
           uni.append(b[i])
    return uni

def main():
    a = []
    b = []
    popula_lista(a)
    popula_lista(b)
    print(uniao(a,b))
    #print(set(a) | set(b))
main()