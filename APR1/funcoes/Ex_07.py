#7) Faça uma função que calcule o fatorial de um número inteiro positivo (faça a consistência). 
#Transforme seus programas de consistência de número já implementados para funções.

def InteiroPositivo(n):
    if n.isdigit():
        if int(n) >= 0:
            return True
    else: 
        return False

def fatorial(num):
    fator = 1
    while num > 0:
        fator *= num
        num -= 1
    return fator

def main():
    num = input("Digite o número que será calculado o fatorial: ")
    while not InteiroPositivo(num):
        print("Valor inserido é inválido")
        num = input("Digite o número de termos da sequência de fibonacci: ")
    else:
        print(f'O fatorial de {num} é {fatorial(int(num))}')

main()