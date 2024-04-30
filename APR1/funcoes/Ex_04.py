def isPositive(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def menu():
    print("Testador de positivo e negativo")
    print("Se o resultado for 1: Número positivo")
    print("Se o resultado for -1: Número negativo")
    print("Se o resultado for 0: Valor 0")
    #print("Caso queira sair do programa digite -9999")

def main():
    menu()
    n = int(input("Digite um número: "))
    result = isPositive(n)
    print(result)
    # while True:
    #     n = int(input("Digite um número: "))
    #     if n == -9999:
    #         return None
    #     result = isPositive(n)
    #     print(result)
main()