#9) Faça uma função que receba uma lista como parâmetro e retorne sua soma.
def isReal(n):
    contador = 0
    numeros = ['0','1','2','3','4','5','6','7','8','9','-','.']
    for i in range(len(n)):
        for j in range(len(numeros)):
            if n[i] == numeros[j]:
                contador += 1
    if contador == len(n):
        return True
    else:
        return False

def somaLista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def main():
    numeros = []
    tam = int(input("Digite o tamanho da lista: "))
    i = 0
    while i < tam:
        num = input(f"Digite a {i+1}ª nota: ")
        if isReal(num):
            numeros.append(float(num))
            i += 1
        else:
            print("Número não real, insira outro valor")
    print(somaLista(numeros))

main()