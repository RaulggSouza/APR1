#8) Faça uma função que retorne a sequencia de Fibonacci recebendo
#como parâmetro o número (faça a consistência) de termos desejado.

def InteiroPositivo(n):
    if n.isdigit():
        if int(n) > 0:
            return True
    else: 
        return False

def fibonacci(num):
    antecessor = 0
    atual = 1
    print(antecessor, end=" ")
    print(atual, end=" ")    
    for i in range(num-2):
        k = atual
        atual += antecessor
        antecessor = k
        print(atual, end=" ")

def main():
    num = input("Digite o número de termos da sequência de fibonacci: ")
    while not InteiroPositivo(num):
        print("Valor inserido é inválido")
        num = input("Digite o número de termos da sequência de fibonacci: ")
    else:
        fibonacci(int(num))

main()