def somar (n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return -1

def potencia(n1,n2):
    return n1**n2

def menu():
    print("Menu de opções da calculadora")
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Potência')
    print('6. Sair')
    op = int(input("Escolhau ma opção entre 1 e 5 ou digite 6 para encerrar o programa"))
    return op

def main():
    opcao = 1
    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            num1 = int(input("Entre com o primeiro número: "))
            num2 = int(input("Entre com o segundo número: "))
            print(somar(num1,num2))
        elif opcao == 2:
            num1 = int(input("Entre com o primeiro número: "))
            num2 = int(input("Entre com o segundo número: "))
            print(subtrair(num1,num2))
        elif opcao == 3:
            num1 = int(input("Entre com o primeiro número: "))
            num2 = int(input("Entre com o segundo número: "))
            print(multiplicar(num1, num2))
        elif opcao == 4:
            num1 = int(input("Entre com o divisor número: "))
            num2 = int(input("Entre com o dividendo número: "))
            print(dividir(num1,num2))
        elif opcao == 5:
            num1 = int(input("Entre com a base número: "))
            num2 = int(input("Entre com o expoente número: "))
            print(potencia(num1,num2))
        elif opcao == 6:
            print("Encerrando o programa...")
        else:
            print("Opção não existente, escolha outra opção entre 1 e 6")


###############PROGRAMA PRINCIPAL######################
main()    