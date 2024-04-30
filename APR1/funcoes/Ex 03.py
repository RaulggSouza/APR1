#3. Elabore a função Real(n) que verifica se o valor de entrada é um número real e retorna TRUE em caso 
#afirmativo e FALSE caso contrário.
def Real(n):
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

def main():
    n = input("Digite um valor: ")
    if Real(n):
        print("É um número real")
    else:
        print("Não é um número real")
    

main()