#2. Elabore a função Inteiro(n) que verifica se o valor de entrada é um
#número inteiro e retorna Verdadeiro em caso afirmativo e Falso caso contrário.
def Inteiro(n):
    contador = 0
    numeros = ['0','1','2','3','4','5','6','7','8','9','-']
    #for valor in n:
        #if valor in numeros:
            #contador += 1
    for i in range(len(n)):
        for j in range(len(numeros)):
            if n[i] == numeros[j]:
                contador += 1
    if contador == len(n):
        return True
    else: 
        return False

def main():
    global n
    n = input("Digite um número: ")
    result = Inteiro(n)
    if result:
        print(f'{n} é um número inteiro')
    else:
        print(f'{n} não é um número inteiro')

main()