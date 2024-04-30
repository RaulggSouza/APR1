#1. Elabore a função InteiroPositivo(n) que verifica se o valor de entrada é um número 
#inteiro positivo e retorna Verdadeiro em caso afirmativo e Falso caso contrário.
def InteiroPositivo(n):
    if n.isdigit():
        if int(n) > 0:
            return True
    else: 
        return False

def main():
    n = input("Digite um número: ")
    result = InteiroPositivo(n)
    if result:
        print(f'{n} é um número inteiro e positivo')
    else:
        print(f'{n} não é um número inteiro e positivo')

main()